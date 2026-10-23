# Challenge 9 — Number Statistics

# User enters numbers.

# Display:
# • Largest
# • Smallest
# • Average
# • Median
# • Second Largest

import statistics
def get_numbers():
    numbers = []
    while True:
        try:
            user_input = input("Enter a number (or 'done' to finish): ")
            if user_input.lower() == 'done':
                break
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers

def display_statistics(numbers):
    if not numbers:
        print("No numbers were entered.")
        return

    sorted_numbers = sorted(numbers)
    largest = max(numbers)
    smallest = min(numbers)
    average = statistics.mean(numbers)
    median = statistics.median(numbers)
    second_largest = sorted_numbers[-2] if len(sorted_numbers) > 1 else None
    try:
        mode = statistics.mode(numbers)
    except statistics.StatisticsError:
        mode = "No unique mode"

    print(f"Sorted Numbers: {sorted_numbers}")
    print(f"Largest Number: {largest}")
    print(f"Smallest Number: {smallest}")
    print(f"Average: {average}")
    print(f"Median: {median}")
    print(f"Second Largest Number: {second_largest}")
    print(f"Mode: {mode}")

def main():
    numbers = get_numbers()
    display_statistics(numbers)

main()