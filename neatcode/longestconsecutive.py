class solution:
    def longestConsecutive(self, nums: list[int]):
        numSet = set(nums)
        longestStreak = 0
        for n in numSet:
            if n-1 not in numSet:
                currentNum = n
                currentStreak = 1
                while currentNum+1 in numSet:
                    currentNum += 1
                    currentStreak += 1
                longestStreak = max(longestStreak, currentStreak)
        return longestStreak

nums = [0,3,7,2,5,8,4,6,0,1]
s = solution()
print(s.longestConsecutive(nums))