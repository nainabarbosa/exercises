# If incr = True and decr = True, then it is a bouncy number. 
def is_bouncy(num):
    incr, decr = False, False
    right_digit = num % 10
    num = num // 10

    while num > 0:
        left_digit = num % 10
        if left_digit < right_digit:
            incr = True
        elif left_digit > right_digit:
            decr = True
        right_digit = left_digit
        num = num // 10
        if incr and decr:
            return True
    return False

# Iterate through numbers until the bouncy count is 99%
count = 0
i = 99
while count < 0.99 * i:
    i = i + 1
    if is_bouncy(i):
        count = count + 1
print(i)
