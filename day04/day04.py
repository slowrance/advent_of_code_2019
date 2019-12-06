# puzzle input is 168630-718098

options = list(range(168630, 718099))

def get_digits(num):
    d1 = num // 100000
    d2 = (num - d1 * 100000) // 10000
    d3 = (num - d1 * 100000 - d2 * 10000) // 1000
    d4 = (num - d1 * 100000 - d2 * 10000 - d3 * 1000) // 100
    d5 = (num - d1 * 100000 - d2 * 10000 - d3 * 1000 - d4 * 100) // 10
    d6 = (num - d1 * 100000 - d2 * 10000 - d3 * 1000 - d4 * 100 - d5 * 10)


    return [d1, d2, d3, d4, d5, d6]

count = 0
for num in options:
    digits = get_digits(num)
    pair_valid = False
    decrease_valid = True
    for idx in range(5):
        if digits[idx] == digits[idx + 1]:
            pair_valid = True
        if digits[idx + 1] < digits[idx]:
            decrease_valid = False
    if pair_valid and decrease_valid:
        print(num)
        count += 1

print(count)


