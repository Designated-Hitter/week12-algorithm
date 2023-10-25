class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        left_max, right_max = [0] * n, [0] * n
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]

        # 계산한 각 위치에서의 왼쪽 높이의 최댓값을 저장
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # 계산한 각 위치에서의 오른쪽 높이의 최댓값을 저장
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        water = 0
        for i in range(n):
            # 현재 위치에서의 물의 높이는 (왼쪽 최댓값과 오른쪽 최댓값 중 작은 것 - 현재 위치의 높이)입니다.
            water += min(left_max[i], right_max[i]) - height[i]

        return water