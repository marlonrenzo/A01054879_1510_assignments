def gcd(a, b):
    a = abs(a)
    b = abs(b)
    remainder = max(a, b) % min(a, b)
    if remainder > 0:
        return gcd(remainder, min(a, b))
    else:
        return min(a, b)


def main():
    print(gcd(25, -5))


if __name__ == '__main__':
    main()
