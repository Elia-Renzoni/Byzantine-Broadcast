import conn as cn
import cluster as group
import byzantine_broadcast as bb

pgroup = group.Cluster()

# match the handler based on req id
def request_strainer(req):
    corruption_status = bb.check_hash(
            req.get_request_hash(),
            req.get_request_content()
    )
    if corruption_status is True:
        return False, "error detected while performing checksum"

    result, message = None, None
    match req.get_request_id():
        case "/join":
            result, message = handle_node_join(req)
        case "/msg":
            result, message = handle_client_message(req)
        case "/replication":
            result, message = handle_replication_message(req)
        case _:
            pass

    return result, message

# this function takes the client requests and
# broadcast them to the entire cluster. The task
# is aborted when the byzantine quorum is not reached
def handle_client_message(req):
    check = bb.ByzantineFault(pgroup.get_cluster_len())
    status, message = check_emptyness(req)
    if status is True:
        return status, message

    # byzantine broadcast the message receivde to all nodes
    peers = pgroup.fetch_membership_list()
    for peer in peers:
        result = bb.send_to(peer, req.get_request_content())
        if result is True:
            check.add_ack()

    if check.is_byzantine_quorum_reached() is True:
        return True, "Byzantine Quorum Reached"

    return False, "Byzantine Quorum Not Reached"

# handler for managing the relayed client request
def handle_replication_message(req):
    message = req.get_request_content()
    print(req.get_request_content())
    
    return True, "task completed"

# this function takes the join request from the
# peers and update the cluster configs
def handle_node_join(req):
    status, message = check_emptyness(req)
    if status is True:
        return status, message
   
    if pgroup.add_node(req.get_request_content()) is True:
        return True, "join completed"
    return False, "join aborted"

def check_emptyness(req):
    if req.get_request_content() is None:
        return True, "empty data"
    return False, ""
