def who_is_missing(file_name):
    with open(file_name, 'r') as file:
        numbers = list(map(int, file.read().split(',')))

    expected_sum = sum(range(1, max(numbers) + 1))
    actual_sum = sum(numbers)
    missing_number = expected_sum - actual_sum

    with open("found.txt", 'w') as out_file:
        out_file.write(str(missing_number))

    return missing_number
