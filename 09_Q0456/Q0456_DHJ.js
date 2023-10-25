/**
 * @param {number[]} nums
 * @return {boolean}
 */
var find132pattern = function(nums) {
    let result = false;
    if (nums.length < 3) {
        return result;
    }

    const n = nums.length;
    const stack = [];

    let third = Number.MIN_SAFE_INTEGER;

    for (let i = n; i >= 0; i--) {
        if (nums[i] < third) {
           result = true;
        }

        while (stack.length > 0 && nums[i] > stack[stack.length - 1]) {
           third = stack.pop();
        }

        stack.push(nums[i]);
    }
    return result;
};