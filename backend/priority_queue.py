def get_next_patient():
    import heapq
    
    if len(queue) == 0:
        return None
    
    return heapq.heappop(queue)