## Python 编程之网上刷题



这里我们用网上评测系统来做做题。英文好的话，可以用`Codeforces`和`LeetCode`。中文可以上计蒜客和力扣。这里用`LeetCode`。

![cf](./img/cf.png)



![jsk](./img/jsk.png)



![leetcode](./img/leetcode.png)





## 1480. Running Sum of 1d Array



> Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.
>
> Return the running sum of `nums`.



```python
class Solution:
    def runningSum(self, nums: [int]) -> [int]:         
      running = []
      s = 0
      for num in nums:
        s += num
        running.append(s)
      
      return running

#print(Solution().runningSum([1,2,3,4]))
```

![ac](./img/ac.png)



第一题通过。



## 1108. Defanging an IP Address



> Given a valid (IPv4) IP `address`, return a defanged version of that IP address.
>
> A *defanged IP address* replaces every period `"."` with `"[.]"`.

```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

# print(Solution().defangIPaddr('1.1.1.1'))
```



## 1431. Kids With the Greatest Number of Candies

> Given the array `candies` and the integer `extraCandies`, where `candies[i]` represents the number of candies that the ***ith\*** kid has.
>
> For each kid check if there is a way to distribute `extraCandies` among the kids such that he or she can have the **greatest** number of candies among them. Notice that multiple kids can have the **greatest** number of candies.



```python
class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        max = 0
        for candy in candies:
          if candy > max:
            max = candy
        greatests = []
        for candy in candies:
          if candy + extraCandies >= max:
            greatests.append(True)
          else:
            greatests.append(False)
        return greatests

# print(Solution().kidsWithCandies([2,3,5,1,3], 3))
```



## 1672. Richest Customer Wealth



> You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount of money the `ith` customer has in the `jth` bank. Return *the **wealth** that the richest customer has.*
>
> A customer's **wealth** is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum **wealth**.



```python
class Solution:
    def maximumWealth(self, accounts: [[int]]) -> int:
        max = 0      
        for account in accounts:
          s = sum(account) 
          if max < s:
            max = s
        return max

#print(Solution().maximumWealth([[1,2,3],[3,2,1]]))          
```



