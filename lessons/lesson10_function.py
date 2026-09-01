# def welcome():
#     print("Добро пожаловать в Python!")

# welcome()
# welcome()
# welcome()

# def hello(name):
#     print("Привет,", name)

# name = str(input("Как тебя зовут? "))
# //тут решение, как я бы сделал немного перефразировав задание
# hello(name)
# // тут решение по описанию задачи
# hello("Влад")
# hello("Андрей")
# hello("Вова")

# def calculate_sum(x, y):
#     return x + y

# result = calculate_sum(10, 30)
# print(result)

# def larger_number(x, y):
#     if x > y:
#         return x
#     else:
#         return y

# print(larger_number(30, 20))

# def evenOrNot(num):
#     if num % 2 == 0:
#         return num

# print(evenOrNot(10))

def turnaround(line):
    N = len(line)
    result = ""
    for index in range(N - 1, -1, -1):
        result += line[index]
    return result

print(turnaround("Лох"))
