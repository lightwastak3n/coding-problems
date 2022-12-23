def test_solution(func, test_input, test_output):
    sol = func(test_input)
    print(f"{'Got:':<10}{sol:>20}\n{'Expected:':<10}{test_output:>20}")
    return sol == test_output


def proceed(func, test_input, test_output, data):
    if test_solution(func, test_input, test_output):
        print(f"Solution: {func(data)}")
    else:
        print("Try again.")
