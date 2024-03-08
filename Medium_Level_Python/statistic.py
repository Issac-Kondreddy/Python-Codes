import statistics
# list of positive integer numbers
datasets = [5, 2, 7, 4, 2, 6, 8]
x = statistics.mean(datasets)
# Printing the mean
print("Mean is :", x)

print("Standard Deviation is :", statistics.stdev(datasets))
print("Median is :", statistics.median(datasets))

print("Mode is :", statistics.mode(datasets))

print(statistics.geometric_mean(datasets))


print(statistics.median_high(datasets))

print(statistics.median_low(datasets))
