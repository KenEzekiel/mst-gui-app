
class prio_queue:
    # Queue element is [value, i, j]
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
    
    def length(self):
        return len(self.queue)
 
    # for inserting an element in the queue
    def enqueue(self, data):
        i = 0
        for i in range(self.length()):
            if data[0] < self.queue[i][0]:
                self.queue.insert(i, data)
                return
        self.queue.insert(self.length(), data)


 
    # for popping an element based on Priority
    def dequeue(self):
        out = self.queue[0]
        self.queue.remove(out)
        return out
    
# q = prio_queue()
# q.enqueue([3])
# q.enqueue([1])
# q.enqueue([2])

# print(q.dequeue())