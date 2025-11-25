import conn as cn
import cluster as group

pgroup = group.Cluster()

# match the handler based on req id
def request_strainer(req):
    corruption_status = compute_checksum(req['checksum'])
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
    data = req['body']
    # to something with the data received.

    # byzantine broadcast the message receivde to all nodes
    peers = pgroup.fetch_membership_list()
    for peer in peers:
        pass
        
    

def handle_replication_message(req):
    pass

def handle_health_check(req):
    pass

def handle_node_join(req):
    if req['body'] is None:
        return False, "empty data"
    
    if pgroup.add_node(req['body']) is True:
        return True, "join completed"
    return False, "join aborted"

def compute_checksum(checksum):
    pass
