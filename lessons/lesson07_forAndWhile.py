# number = int(input("Введите число: "))

# for number in range(1, number + 1):
#     print(number)

# number = int(input("Введите число: "))
# sum = 0
# for number in range(1, number + 1):
#     sum = sum + number
# print(sum)

# number = int(input("Введите число: "))

# for number in range(1, number + 1):
#     if number % 2 == 0:
#         print(number)

# numbers = [12, 5, 8, 21, 4, 17, 30]
# res = 0

# for number in numbers:
#     if number % 2 == 0:
#         res+=1
# print(res)

numbers = [12, 5, 8,50, 21, 4, 17, 30]
maxNumber = 0
for number in numbers:
    if number >= maxNumber:
        maxNumber = number
print(maxNumber)