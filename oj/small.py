# class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        ss = sorted((e,i) for i,e in enumerate(nums))

        l = len(nums)
        last = 0
        ns = [0]*l
        for i in range(1, l):
          (e0, j0) = ss[i-1]
          (e1, j1) = ss[i]
          if e0 == e1:
            pass
          else:
            last = i

          ns[j1] = last
        return ns

# print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))