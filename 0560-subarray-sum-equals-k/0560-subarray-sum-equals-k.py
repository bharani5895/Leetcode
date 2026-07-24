class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        psa=0
        hash_map={}
        count=0
        hash_map[0]=1
        for i in range(len(arr)):
            psa+=arr[i]

            
            a=psa
            if a-k in hash_map:
                count+=hash_map.get(a-k)

            
            if a in hash_map:
                hash_map[a]=hash_map.get(a,0)+1
                
            else:
                hash_map[a]=1
            
        return count
        
        