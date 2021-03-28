class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_num = 0
        
        for banks in accounts:
            num = 0
            for bank in banks:
                num += bank
            max_num = max(max_num, num)
        
        return max_num
