import heapq
class Solution:
    def maxSubsequence(self, n: List[int], k: int) -> List[int]:
        p=[]
        heapq.heapify(p)
        for i in range(len(n)):
            heapq.heappush(p,[n[i],i])
            if len(p)>k:
                heapq.heappop(p)
            
        p.sort(key=lambda x:x[1])
        res=[]
        for i in range(len(p)):
            res.append(p[i][0])
        return res