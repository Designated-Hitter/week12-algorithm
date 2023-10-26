class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [-1, -1]
        try:
            a = nums.index(target)
            nums = nums[::-1]
            b = nums.index(target)
            answer = [a, (len(nums) - 1) - b]
        except:
           return answer
        return answer