def add_squares_of_even():
    sum_ = 0
    for i in range(1, 51):
        sum_ += i ** 2 if i % 2 == 0 else 0
    return sum_

print(f"Sum of squares of all even numbers between 1 to 51: {add_squares_of_even()}")