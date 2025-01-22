from statistics import mean, mode, median, variance, stdev

ratings = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

print("Frequency of each rating:")
for i in range(1, 6):
    print(f"Rating {i}: {ratings.count(i)} times")

minimum = min(ratings)
maximum = max(ratings)
range_ = maximum - minimum
mean_ = mean(ratings)
median_ = median(ratings)
mode_ = mode(ratings)
variance_ = variance(ratings)
standard_deviation = stdev(ratings)

print(f"\nMinimum rating: {minimum}")
print(f"Maximum rating: {maximum}")
print(f"Range: {range_}")
print(f"Mean: {mean_}")
print(f"Median: {median_}")
print(f"Mode: {mode_}")
print(f"Variance: {variance_:.2f}")
print(f"Standard Deviation: {standard_deviation:.2f}")