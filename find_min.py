numbers = [34,432,1,99]

loser = 1

for number in numbers:
    if number < loser:
        loser = number

print(loser)