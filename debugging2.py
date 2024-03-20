def calculateAverage(numbers):
    sum = 0
    for number in numbers:
       sum += number
    return sum / len(numbers)


numbers = [10, 20, 30, 40, 50]
avg = calculateAverage(numbers)
print(f"The average is: {int(avg)}")


