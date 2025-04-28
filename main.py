user_input = list(map(int, input("please enter your numbers: ").split()))

def even_numbers(user_input):
    result = []
    for num in user_input:
        if num % 2 == 0:
            result.append(num)
    return result

def max_num(user_input):
    current_max = user_input[0]
    for i in range(1, len(user_input)):
        if user_input[i] > current_max:
            current_max = user_input[i]
    return current_max

def min_num(user_input):
    current_min = user_input[0]
    for i in range(1, len(user_input)):
        if user_input[i] < current_min:
            current_min = user_input[i]
    return current_min

def sorting(user_input):
    for i in range(len(user_input)):
        for j in range(i +1, len(user_input)):
            if user_input[i] > user_input[j]:
                user_input[i], user_input[j] = user_input[j], user_input[i]
    return user_input

print(f"Четные числа: {even_numbers(user_input)}")
print(f"Минимальное число: {min_num(user_input)}")
print(f"Максимальное число: {max_num(user_input)}")
print(f"Отсортированный список {sorting(user_input)}")
