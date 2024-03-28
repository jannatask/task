Дан целочисленный массив nums длины n, вам нужно создать массив ans 
длины 2n, где ans[i] == nums[i] и ans[i + n] == nums[i] для 0 <= i < n (индекс 0).

В частности, ans — это объединение двух массивов чисел.

Вернуть массив ans.


Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
'''
def ans(nums):
   n = len(nums)
   ans = nums * 2
   return ans
nums = [1,2,3,4,5]
ans = ans(nums)
print(ans)

'''
Дан массив nums, создайте массив ans той же длины, 
где ans[i] = nums[nums[i]] для каждого 0 <= i < nums.length, и верните его.

Перестановка nums, начинающаяся с нуля, представляет собой массив различных целых чисел 
от 0 до nums.length - 1 (включительно).

Example 1:
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
    
Example 2:
Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]
'''
def permutation(nums):
    n = len(nums)
    ans = [0] * n
    
    for i in range(n):
        ans[i] = nums[nums[i]]
    
    return ans
nums1 = [0, 2, 1, 5, 3, 4]
print(permutation(nums1)) 

nums2 = [5, 0, 1, 2, 3, 4]
print(permutation(nums2))  

'''
Вам дано неотрицательное число с плавающей запятой, округленное до двух десятичных знаков Цельсия, 
которое обозначает температуру в Цельсиях.

Вам следует преобразовать градусы Цельсия в Кельвины и Фаренгейты и вернуть их в виде массива
 ans = [кельвин, градусы Фаренгейта].

Вернуть массив ans. Принимаются ответы в пределах 10-5 от фактического ответа.

Обратите внимание, что:

Kelvin = Celsius + 273.15
Fahrenheit = Celsius * 1.80 + 32.00

Example 1:
Input: celsius = 36.50
Output: [309.65000,97.70000]
Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.

Example 2:
Input: celsius = 122.11
Output: [395.26000,251.79800]
Explanation: Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.

'''
def temperature_conversion(celsius):
    kelvin = round(celsius + 273.15, 5)
    fahrenheit = round(celsius * 1.8 + 32.0, 5)
    return [kelvin, fahrenheit]

celsius1 = 36.50
print(temperature_conversion(celsius1))

celsius2 = 122.11
print(temperature_conversion(celsius2))



