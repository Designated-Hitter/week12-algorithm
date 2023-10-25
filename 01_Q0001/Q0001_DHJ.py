# 1. 반복문을 사용한 O(N^2) 풀이
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            other = target - nums[i]
            
            for j in range(len(nums)):
                if other == nums[j]:
                    if i != j:
                        return [i, j]

# 2. dictionary를 사용한 풀이
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
    
        for i, num in enumerate(nums):
            complement = target - num
            # 보완되는 숫자가 딕셔너리에 있는 경우, 해당 숫자의 인덱스와 현재 숫자의 인덱스를 반환
            if complement in num_to_index:
                return [num_to_index[complement], i]