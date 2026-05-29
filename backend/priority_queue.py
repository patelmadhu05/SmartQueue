import heapq

queue = []

def add_patient(name, priority):
    heapq.heappush(queue, (priority, name))

def get_next_patient():
    if len(queue) == 0:
        return None
    return heapq.heappop(queue)

# NEW: Helper function to get a perfectly sorted copy of the queue for the UI
def get_sorted_queue():
    # Creating a sorted copy so we don't destroy the original heap
    return sorted(queue)