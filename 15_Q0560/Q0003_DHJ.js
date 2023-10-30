/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let output = 0;
    let sum = 0;
    const sumCounts = new Map();
    //sum 과 k의 값이 바로 일치하는 경우를 위해
    sumCounts.set(0, 1);
    // sum을 set의 key 로 삼고 value를 변경한다.
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i]
        //sum과 k가 일치한다면 output 추가
        if (sumCounts.has(sum - k)) {
            output += sumCounts.get(sum - k)
        }
        
        if (sumCounts.has(sum)) {
            sumCounts.set(sum, sumCounts.get(sum) + 1);
        } else {
            sumCounts.set(sum, 1);
        }
    }
    return output;
};