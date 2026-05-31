from queue import PriorityQueue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        pq=PriorityQueue()
        for ele in stones:
            pq.put(-ele)
        
        print(pq)
        while pq.qsize()>1:
            y=-pq.get()
            x=-pq.get()
            if x==y:
                continue
            else:
                pq.put(-(y-x))
        
        return -pq.queue[0] if pq.qsize()==1 else 0

        

        