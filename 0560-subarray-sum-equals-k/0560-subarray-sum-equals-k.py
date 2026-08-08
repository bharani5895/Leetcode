class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:

        
        

        map = {0: 1}
        
        cursum = 0
        count = 0
        
        for x in arr:
            cursum += x
            
            need = cursum - k
            
            if need in map:
                count = count + map[need]
            
            map[cursum] = map.get(cursum, 0) + 1
        
        return count