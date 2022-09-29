# 要求四：
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
# 提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。
def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
  # 設定一開始最大值為零
  maxnumber = 0
  # 設定相乘的數字一開始為零，其會一直變動並拿來和最大值比較
  productnumber = 0

  for i in range(len(nums)):
    # 下限包含，上限不包含
    for j in range(i+1,len(nums)):
      productnumber = nums[i] * nums[j]
      # 第一個數跟第二個數相乘先指派為最大值
      if ( i==0 and j==1):
        maxnumber = productnumber
      if (productnumber > maxnumber):
        maxnumber = productnumber
        
  print(maxnumber)


  
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10
