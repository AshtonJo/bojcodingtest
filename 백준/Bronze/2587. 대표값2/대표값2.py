num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

total_sum = num1 + num2 + num3 + num4 + num5
arr = [num1, num2, num3, num4, num5]

average = total_sum // 5
arr.sort()
middle = arr[len(arr) // 2]

print(average)
print(middle)