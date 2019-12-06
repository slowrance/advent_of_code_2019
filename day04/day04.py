# puzzle input is 168630-718098

# 896 too low for part 2

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
    triple_valid = True
    decrease_valid = True
    for digit in digits:
        if digits.count(digit) == 2:
            pair_valid = True
    for idx in range(6):
        if idx < 5:
            if digits[idx + 1] < digits[idx]:
                decrease_valid = False
        # if idx < 2:
        #     continue
        # if digits[idx] == digits[idx - 1] and digits[idx] != digits[idx - 2]:
        #     pair_valid = True
        # if digits[idx] == digits[idx - 1] and digits[idx] == digits[idx - 2]:
        #     triple_valid = False
        #     pair_valid = False



    if pair_valid and decrease_valid:
        print(num)
        count += 1

print(count)


