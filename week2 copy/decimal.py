def val(c):
    if (c >= '0' and c <= '9'):
        return ord(c) - 48
    else:
        return ord(c) - 65 + 10


def to_decimal(s, base):
    lenn = len(s)
    power = 1
    num = 0
    for i in range(lenn-1, -1, -1):
        if base < 0:
            print("Error: negative base")
            return ""
        elif '-' in s:
            print("Error: negative number")
            return ""
        elif base > 36:
            print("Error: base > 36")
            return ""
        elif (val(s[i]) >= base or base == 0):
            print("Error: incorrect number/base")
            return ""
        num += val(s[i]) * power
        power = power * base
    return num


def re_val(num):
    if (num >= 0 and num <= 9):
        return chr(num + 48)
    else:
        return chr(num - 10 + 65)


def from_decimal(s, b):
    if b < 0:
        return "Error: negative base"
    elif s < 0:
        return "Error: negative number"
    elif b > 36:
        return "Error: base > 36"
    r = ""
    while (s > 0):
        r += re_val(s % b)
        s //= b

    r = r[::-1]
    return r


print(to_decimal("1BJ", 26))
print(from_decimal (23,2))
print(from_decimal (230,16))
print(from_decimal (2345,26))
print(to_decimal('5',0))
print(to_decimal('-12', 16))
print(to_decimal('A', -16))
print(to_decimal('45',37))
