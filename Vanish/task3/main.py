def sort_digits(digits):
    amount_digits = dict()
    for digit in digits:
        if digit in amount_digits.keys():
            amount_digits[digit] += 1
        else:
            amount_digits[digit] = 1

    amount_digits = tuple(amount_digits.items())
    amount_digits = sorted(amount_digits, key=lambda x: (x[1], -x[0]), reverse=True)
    amount_digits = [i[0] for i in amount_digits]
    return amount_digits


def main():
    output_text = ''
    with open('input.txt') as fin:
        for line in fin:
            digits = map(int, line.split())
            digits = sort_digits(digits)
            for d in digits:
                output_text += f'{d} '
            output_text += '\n'

    with open('output.txt', 'w') as fout:
        fout.write(output_text)


if __name__ == '__main__':
    main()