class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]]
        for i in range(1, len(intervals)):
            cur_intervals = intervals[i]
            last_intervals = answer[-1]
            if cur_intervals[0] <= last_intervals[1]:
                last_intervals[1] = max(last_intervals[1], cur_intervals[1])
            else:
                answer.append(cur_intervals)

        return answer