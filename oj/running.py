class Solution:
    def runningSum(self, nums: [int]) -> [int]:         
      running = []
      s = 0
      for num in nums:
        s += num
        running.append(s)
      
      return running

print(Solution().runningSum([1,2,3,4]))