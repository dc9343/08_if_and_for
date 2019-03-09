numbers = [34,432,1,99]

champion = numbers[0]

for number in numbers:
    if number < champion:
        champion = number

print(champion)
