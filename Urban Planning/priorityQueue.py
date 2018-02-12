import heapq

#The class for the PriorityQueue (lowest in the top)
class PriorityQueue:
    def __init__ (self):
        #Elements
        self.queue = []
        #Number of elements
        self.index = 0

    def push(self, Node, priority):
        #Add element to the queue with its priority
        heapq.heappush(self.queue,(priority,self.index,Node))
        #Increase index
        self.index += 1

    def pop(self):
        #decrease index
        self.index -= 1
        #Pop node in the top of queue
        return heapq.nlargest(1,self.queue)[-1]
        # return heapq.heappop(self.queue)[-1]

    def popMin(self):
        #decrease index
        self.index -= 1
        #Pop node in the top of queue
        return heapq.heappop(self.queue)[-1]

    def __len__(self):
        return len(self.queue)

    def __getitem__(self, item):
        return self.queue[item]