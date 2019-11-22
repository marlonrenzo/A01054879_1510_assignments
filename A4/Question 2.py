def gcd(a, b):
    remainder = max(abs(a), abs(b)) % min(abs(a), abs(b))
    if remainder > 0:
        return gcd(remainder, min(abs(a), abs(b)))
    return min(abs(a), abs(b))


def main():
    print(gcd(270, 192))


if __name__ == '__main__':
    main()
