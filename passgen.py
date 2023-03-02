import random as rd
import argparse as argp


def create_lsts():
    word_file = (open("words.txt", "r").readlines())
    words = []
    for i in word_file:
        words.append(i.replace("\n", ""))
        i.lower()

    num_lst = list(range(10))
    num_lst = [str(i) for i in num_lst]
    sym_lst = ["!", "?", "@", "#", "$", "%", "&", "*", "(", ")", "-", "+", "=", ";", ":"]

    return words, num_lst, sym_lst


def parse_args():
    parser = argp.ArgumentParser(description='Password Generator')
    parser.add_argument('-w', '--words', type=int, help='include WORDS words.txt in the password (default=4)')
    parser.add_argument('-n', '--numbers', type=int, help='insert NUMBERS random numbers in the password (default=0)')
    parser.add_argument('-s', '--symbols', type=int, help='insert SYMBOLS random symbols in the password (default=0)')
    parser.add_argument('-c', '--caps', type=int, help='capitalize the first letter of CAPS random words.txt (default=0)')

    return parser.parse_args()


def main():
    pass_lst = []
    words, nums, syms = create_lsts()
    args = parse_args()
    if args.words:
        w = rd.choices(words, k=args.words)
    else:
        w = rd.choices(words, k=4)
    if args.numbers:
        n = rd.choices(nums, k=args.numbers)
    else:
        n = ""
    if args.symbols:
        s = rd.choices(syms, k=args.symbols)
    else:
        s = ""
    if args.caps:
        if args.caps < len(w):
            for i, cap in enumerate(w[:args.caps]):
                w[i] = cap.capitalize()
    pass_lst.extend(w)
    pass_lst.extend(n)
    pass_lst.extend(s)
    rd.shuffle(pass_lst)
    password = "".join(pass_lst)

    print(password)


main()
