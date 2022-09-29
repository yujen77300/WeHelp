// 要求四：
// 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
// 提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。
function maxProduct(nums) {
  // 請用你的程式補完這個函式的區塊
  // 設定一開始最大值為零
  let maxnumber = 0
  // 設定相乘的數字一開始為零，其會一直變動並拿來和最大值比較
  let productnumber = 0
  for (let i = 0; i < nums.length; i++) {
    // 下限包含，上限不包含
    for (let j = i + 1; j < nums.length; j++) {
      productnumber = nums[i] * nums[j]
      // 第一個數跟第二個數相乘先指派為最大值
      if (i === 0 && j === 1) {
        maxnumber = productnumber
      }
      if (productnumber > maxnumber) {
        maxnumber = productnumber
      }
    }
  }
  console.log(maxnumber)
}





maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([10, -20, 0, -3]) // 得到 60
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0 或 -0
maxProduct([5, -1, -2, 0]) // 得到 2
maxProduct([-5, -2]) // 得到 10
