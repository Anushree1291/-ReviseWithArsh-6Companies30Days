class Solution:
    def frequencySort(self, s: str) -> str:
        m={}
        
        for i in s:
            if i not in m:
                m[i]=0
            m[i]+=1
            
        s=""
        for i in sorted(m,key=m.get,reverse=True):
            s+=i*m[i]
        
        return s