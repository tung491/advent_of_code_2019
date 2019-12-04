def main():
    result = []
    for n in range(108457, 562042):
        digits = [int(digit) for digit in list(str(n))]
        double = False
        increase_seq = False
        for i in range(len(digits) - 1):
            if digits[i] == digits[i+1] and str(digits[i]) * 3 not in str(n):
                double = True
                break
        if sorted(digits) == digits:
            increase_seq = True
        if double and increase_seq:
            result.append(n)
    return len(result)

if __name__ == "__main__":
    print(main())
