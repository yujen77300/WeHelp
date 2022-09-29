// 要求二：JavaScript 物件與陣列
// 完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中
// manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量
// 不定的情況。
function avg(data) {
  // 請用你的程式補完這個函式的區塊
  let nonmanager = 0
  let total_salary = 0
  // 用Array的屬性 length取得長度
  for (let i = 0; i < data.employees.length; i++) {
    if (data.employees[i].manager === false) {
      nonmanager += 1
      total_salary += data.employees[i].salary
    }
  }
  console.log(total_salary / nonmanager)
}


avg({
  "employees": [
    {
      "name": "John",
      "salary": 30000,
      "manager": false
    },
    {
      "name": "Bob",
      "salary": 60000,
      "manager": true
    },
    {
      "name": "Jenny",
      "salary": 50000,
      "manager": false
    },
    {
      "name": "Tony",
      "salary": 40000,
      "manager": false
    }
  ]
}); // 呼叫 avg 函式
