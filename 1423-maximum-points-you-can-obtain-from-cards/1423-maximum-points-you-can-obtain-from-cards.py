class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        # Take all k cards from the left first
        current_sum = sum(cardPoints[:k])
        max_sum = current_sum
        
        # Swap cards from the left side with cards from the right side one by one
        for i in range(1, k + 1):
            current_sum += cardPoints[-i] - cardPoints[k - i]
            max_sum = max(max_sum, current_sum)
            
        return max_sum