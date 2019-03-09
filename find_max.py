#最大値を求める　if 使う

numbers = [34,432,1,99]

champion = 0

for number in numbers:
    if number > champion:
        champion = number

print(champion)
