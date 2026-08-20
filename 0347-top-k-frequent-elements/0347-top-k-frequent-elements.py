class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        # Count frequency
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        ans = []

        # Find k highest frequencies
        for i in range(k):
            max_freq = 0
            max_element = 0

            for x in freq:
                if freq[x] > max_freq:
                    max_freq = freq[x]
                    max_element = x

            ans.append(max_element)

            # Remove it so we don't select it again
            del freq[max_element]

        return ans