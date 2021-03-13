class Solution:
    def maximumWealth(self, accounts: [[int]]) -> int:
        max = 0      
        for account in accounts:
          s = sum(account) 
          if max < s:
            max = s
        return max

#print(Solution().maximumWealth([[1,2,3],[3,2,1]]))
          