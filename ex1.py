# Write a function that takes a list of numbers and returns a tuple containing (min, max, average) of the numbers.


#min
def find_minimum_value(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

#max    
def find_maximum_value(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value  = num
    return max_value

#avg
def calculate_average(numbers):
    total_sum = sum(numbers)
    average = total_sum/len(numbers)
    return average

#tuple
def analyze_numbers(numbers):
    if not numbers:
        return 0, 0, 0
    min_num = find_minimum_value(numbers)
    max_num = find_maximum_value(numbers)
    avg_num = calculate_average(numbers)
    return min_num, max_num, avg_num

#Example
my_numbers = [5, 2, 9, 1, 7]
min_v, max_v, avg_v = analyze_numbers(my_numbers)
print(f"Minimum: {min_v}")
print(f"Maximum: {max_v}")
print(f"Average: {avg_v}")