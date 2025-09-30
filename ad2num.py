def add2num(num1, num2):
    num1 = list(map(int, str(num1)))
    num2 = list(map(int, str(num2)))
    num1.reverse()
    num2.reverse()
    # Pad the shorter list with zeros
    if len(num1) < len(num2):
        num1 += [0] * (len(num2) - len(num1))
    else:
        num2 += [0] * (len(num1) - len(num2))
    carry = 0
    result = []
    for d1, d2 in zip(num1, num2):
        total = d1 + d2 + carry
        result.append(total % 10)
        carry = total // 10
    if carry:
        result.append(carry)
    result.reverse()
    return result

print(add2num(123, 343))