def calculate_filtered_mean(numbers, lower_threshold=0, upper_threshold=1):
    normalized_values = [round(value / max(numbers), 2) for value in numbers]
    filtered_values = [value for value in normalized_values if lower_threshold <= value <= upper_threshold]
    mean = sum(filtered_values) / len(filtered_values) if filtered_values else 0
    return filtered_values, mean


numbers = [1, 2, 3]

filtered_values, mean = calculate_filtered_mean(numbers)

print("Input numbers:", numbers)
print("Filtered and normalized values:", filtered_values)

lower_threshold = 0.5
upper_threshold = 1
filtered_values, mean = calculate_filtered_mean(numbers, lower_threshold, upper_threshold)

print("Thresholds: lower =", lower_threshold, "upper =", upper_threshold)
print("Filtered and normalized values within thresholds:", filtered_values)
print("Mean of filtered values:", round(mean, 2))