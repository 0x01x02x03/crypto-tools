# Author: w3ndige
# Reimplementation of pablocelayes tool 

def is_perfect_square(n):
    h = n & 0xF;

    if h > 9:
        return -1

    if ( h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8 ):
        t = isqrt(n)
        if t*t == n:
            return t
        else:
            return -1

    return -1

def isqrt(n):
    if n < 0:
        raise ValueError('Number must be >= 0')

    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def bitlength(x):
    assert x >= 0
    n = 0
    while x > 0:
        n = n+1
        x = x>>1
    return n

def get_cf_expansion(n, d):
    quotients = []

    q = n // d
    r = n % d
    quotients.append(q)

    while r != 0:
        n, d = d, r
        q = n // d
        r = n % d
        quotients.append(q)

    return quotients

def get_convergents(e):
    nominators = []
    denominators = []

    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else:
            ni = e[i] * nominators[i-1] + nominators[i-2]
            di = e[i] * denominators[i-1] + denominators[i-2]

        nominators.append(ni)
        denominators.append(di)
        yield (ni, di)

def attack(e, n):
    cf_expansion = get_cf_expansion(e, n)
    convergents = get_convergents(cf_expansion)

    for (k,d) in convergents:
        if k != 0 and (e * d-1) % k == 0:
            phi = (e * d-1) // k
            s = n - phi + 1
            discr = s*s - 4*n
            if (discr >= 0):
                t = is_perfect_square(discr)
                if t != -1 and (s+t) % 2 == 0:
                    print("Hacked D ")
                    return d

def main():
    print("Welcome to RSA Wiener attack")
    e = int(input("Enter e: "))
    n = int(input("Enter n: "))

    print(attack(e, n))


if __name__ == '__main__':
    main()
