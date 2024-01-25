import math

def mean(data):
    return sum(data) / len(data)

def pearson_correlation(x, y):
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)

    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = math.sqrt(sum((xi - mean_x)**2 for xi in x) * sum((yi - mean_y)**2 for yi in y))

    if denominator == 0:
        return 0  # В случае нулевого делителя возвращаем 0

    return numerator / denominator

# Пример использования
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]

correlation = pearson_correlation(array1, array2)
print(f"Pearson correlation coefficient: {correlation}")
