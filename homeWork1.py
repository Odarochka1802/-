# Вот пример императивной процедуры сортировки списка чисел в порядке убывания,
# используя пузырьковую сортировку

import time
numbers = [i for i in range(0, 1000)]
def bubble_sort_desc(numbers):
    start_time = time.time()  # Замеряем время начала выполнения функции
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    end_time = time.time()  # Замеряем время окончания выполнения функции
    print(f"Время выполнения bubble_sort_desc: {end_time - start_time} сек")


bubble_sort_desc(numbers)
print(numbers)


# В декларативном стиле можно воспользоваться функцией sorted с параметром
# reverse=True, чтобы отсортировать список чисел в порядке убывания.

numbers2 = [i for i in range(0, 1000)]

def sort_numbers_desc(numbers2):
    start_time = time.time()  # Замеряем время начала выполнения функции
    numbers2.sort(reverse=True)
    end_time = time.time()  # Замеряем время окончания выполнения функции
    print(f"Время выполнения sort_numbers_desc: {end_time - start_time} сек")


sort_numbers_desc(numbers2)
print(numbers2)