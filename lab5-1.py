def calculate_mean(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

def format_mean(mean):
    formatted_mean = "{:.2f}".format(mean)
    return formatted_mean

number_list = [3, 5, 2, 8, 1, 9]
mean_value = calculate_mean(number_list)
formatted_mean_value = format_mean(mean_value)
print("Mean value:", formatted_mean_value)
