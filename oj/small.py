class Solution:
 
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
      max_num =max(nums)

      n = [0] * (max_num + 1)
      for num in nums:
        n[num] += 1

      sorted_ls = []
      for i in range(max_num + 1):
        if n[i] > 0:
          sorted_ls.append(i)

      sm = [0] * (max_num + 1)
      sum = 0
      for i in range(len(sorted_ls)):
        v = sorted_ls[i]
        sm[v] = sum
        sum += n[v]
      
      ns = [] 
      for i in range(len(nums)):
        ns.append(sm[nums[i]])
      return ns


# print(Solution().smallerNumbersThanCurrent([72,48,32,16,10,59,83,38,1,4,68,7,67,16,5,35,99,15,55,11,24,3,63,81,16,95,35,87,24,84,57,49,42,80,34,33,82,81,31,31,7,75,100,75,22,44,54,77,89,71,81,66,7]))