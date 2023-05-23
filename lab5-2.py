def calculate_mean(numbers, lower_threshold=0, upper_threshold=1):
    normalized_numbers = [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]
    filtered_numbers = [x for x in normalized_numbers if lower_threshold <= x <= upper_threshold]
    mean = sum(filtered_numbers) / len(filtered_numbers)
    return round(mean, 2)

# Example usage
number_list = [3, 5, 2, 8, 1, 9]
lower_thresh = 0.2
upper_thresh = 0.8
mean_value = calculate_mean(number_list, lower_threshold=lower_thresh, upper_threshold=upper_thresh)
print("Mean value:", mean_value)
