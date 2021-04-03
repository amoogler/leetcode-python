class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(list(jewels))
        jewels_num = 0
        
        for stone in stones:
            if stone in jewels_set:
                jewels_num += 1
        
        return jewels_num
