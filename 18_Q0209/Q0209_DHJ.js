/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let answer = Infinity;
    let left = 0;
    let sum = 0;

    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];

        while (sum >= target) {
            answer = Math.min(answer, right - left + 1);
            sum -= nums[left];
            left++;
        }
    }

    if (answer === Infinity) {
        return 0;
    } else {
        return answer;
    }
};