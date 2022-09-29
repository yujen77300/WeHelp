# 要求六 ( Optional )：
# 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。

def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
# 連續出現0的最大長度
  longestzero = 0
# 出現0的長度，會根據i重新歸零再計算
  lengthofzero = 0
  for i in range(len(nums)):
    if (nums[i] == 0 ): 
      lengthofzero += 1
      for j in range(i+1,len(nums)):
        if nums[j] == 0 :
          lengthofzero +=1
        else:
          break
      if lengthofzero > longestzero:
        longestzero = lengthofzero
    # 用來比較的變數要歸零
      lengthofzero = 0
  print(longestzero)  

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
