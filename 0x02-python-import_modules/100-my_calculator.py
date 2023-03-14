#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1, sys
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    plus = calculator_1.add(a, b)
    minu = calculator_1.sub(a, b)
    mult = calculator_1.mul(a, b)
    divi = calculator_1.div(a, b)
    if op == "+":
        print("{} + {} = {}".format(a, b, plus))
    elif op == "-":
        print("{} - {} = {}".format(a, b, minu))
    elif op == "*":
        print("{} * {} = {}".format(a, b, mult))
    elif op == "/":
        print("{} / {} = {}".format(a, b, div))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
