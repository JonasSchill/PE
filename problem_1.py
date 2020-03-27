#Multiples of 3 and 5

target = 1000

def sum_divisible_by(n):
    num = (target - 1) // n
    return n * (num * (num + 1)) // 2

sum = sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)

print(sum)