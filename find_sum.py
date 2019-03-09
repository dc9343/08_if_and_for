numbers = [34, 432, 1, 99]

# numbersの合計値をfor を使って出力してください

# 合計を出す
# forを使う

#回答例1　
total = 0
total = total + numbers[0]
total = total + numbers[1]
total = total + numbers[2]
total = total + numbers[3]

print(total)
#回答例2
total = 0

for number in numbers:
    total = total + number

print(total)

#回答例3
total = 0
for number in numbers:
    total += number

print(total)