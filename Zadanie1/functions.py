def roundToSpecifiedPlace(data, r):
    return f'{round(data, r):.{r}f}'

def arithmeticMean(list):
    sum = 0
    count = 0
    for i in list:
        count += 1
        sum += i
    return roundToSpecifiedPlace(sum / count, 2)

def standardDeviation(list):
    mean = sum(list) / len(list)
    variance = sum((x - mean) ** 2 for x in list) / (len(list) - 1)
    return roundToSpecifiedPlace(variance ** 0.5, 2)

def median(list):
    list.sort()
    n = len(list)
    middle = n // 2
    if n % 2 == 0:
        return roundToSpecifiedPlace((list[middle - 1] + list[middle]) / 2, 2)
    else:
        return roundToSpecifiedPlace(list[middle], 2)

def quartile(list, q):
    list.sort()
    index = int(q * len(list))
    return roundToSpecifiedPlace(list[index], 2)

def PearsonsLinearCorrelation(list_x, list_y):
    list_x_mean = sum(list_x) / len(list_x)
    list_y_mean = sum(list_y) / len(list_y)

    numerator = sum((x - list_x_mean) * (y - list_y_mean) for x, y in zip(list_x, list_y))

    sum_square_x = sum((x - list_x_mean) ** 2 for x in list_x)
    sum_square_y = sum((y - list_y_mean) ** 2 for y in list_y)

    denominator = (sum_square_x * sum_square_y) ** 0.5

    correlation = numerator / denominator

    return correlation

def linearRegressionEquation(list_x, list_y):
    list_x_mean = sum(list_x) / len(list_x)
    list_y_mean = sum(list_y) / len(list_y)

    numerator = sum((x - list_x_mean) * (y - list_y_mean) for x, y in zip(list_x, list_y))
    denominator = sum((x - list_x_mean) ** 2 for x in list_x)
    a = numerator / denominator

    b = list_y_mean - a * list_x_mean

    return a, b