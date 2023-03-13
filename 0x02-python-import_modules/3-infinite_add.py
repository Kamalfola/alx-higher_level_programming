#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
s = 0
for i in range(count):
    a = int(sys.argv[i + 1])
    s += a

print("{}".format(s))
