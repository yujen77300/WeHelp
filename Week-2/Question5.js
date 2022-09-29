// 要求五：
// Given an array of integers, show indices of the two numbers such that they add up to a
// specific target. You can assume that each input would have exactly one solution, and you
// can not use the same element twice.

function twoSum(nums, target) {
  // your code here
  let result = []
  // console.log(nums[0])

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      // console.log(nums[j])
      if (nums[i] + nums[j] === target) {
        result.push(i)
        result.push(j)
        break
      }
    }
  }
  return result

}


let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9
