import heapq

queue = []

def add_patient(name, priority):
    heapq.heappush(queue, (priority, name))