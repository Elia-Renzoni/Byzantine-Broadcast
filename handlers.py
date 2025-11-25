import conn as cn
import cluster as group
import byzantine_broadcast as bb

pgroup = group.Cluster()

# match the handler based on req id
def request_strainer(req):
    corruption_status = bb.perform_checksum(req['checksum'])
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

def handle_client_message(req):
    check = bb.ByzantineFault()
    status, message = check_emptyness(req)
    if status is True:
        return status, message

    # byzantine broadcast the message receivde to all nodes
    peers = pgroup.fetch_membership_list()
    for peer in peers:
        result = bb.send_to(peer, data)
        if result is True:
            check.add_ack()

    if check.is_byzantine_quorum_reached() is True:
        return True, "Byzantine Qurorum Reached"

    return False, "Byzantine Quorum Not Reached"

def handle_replication_message(req):
    pass

def handle_health_check(req):
    pass

def handle_node_join(req):
    status, message = check_emptyness(req)
    if status is True:
        return status, message
   
    if pgroup.add_node(req['body']) is True:
        return True, "join completed"
    return False, "join aborted"

def check_emptyness(req):
    if req['body'] is None:
        return True, "empty data"
    return False, ""
