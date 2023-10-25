/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    result = [];
    nums.sort((a, b) => a - b);
    const n = nums.length;
    for (let i = 0; i < n - 2; i++) {
        // 중복된 값 건너뛰기
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }
    // 나머지 두 숫자를 찾는 포인터들
        let left = i + 1;
        let right = n - 1;

        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];

            if (sum === 0) {
                result.push([nums[i], nums[left], nums[right]]);
                
                // 중복된 값 건너뛰기
                while (left < right && nums[left] === nums[left + 1]) {
                    left++;
                }
                while (left < right && nums[right] === nums[right - 1]) {
                    right--;
                }

                // 다음 유일한 값으로 이동
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

    return result;
}