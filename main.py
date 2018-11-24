def re(num):
    ''' Extract a = Re(num). '''
    a = num[:num.find(' ')]
    return float(a)


def im(num):
    ''' Extract b = Im(num). '''
    b = num[num.find(' ') + 3:num.find('i')]
    return float(b)


def mod(a, b):
    ''' Complex number module. '''
    return (a**2+b**2)**.5


def arg(a, b):
    ''' Complex number argument. '''
    import math
    return (math.atan(b/a)*180)/math.pi


def trig(r, fi):
    ''' Trigonometric form. '''
    print('Trigonometric form: {0}*(cos({1}) + i*sin({1}))'
          .format(round(r, 2), round(fi, 2)))


def power(r, fi, exp):
    ''' Power of complex number. '''
    print('To the {2} degree: {0}*(cos({1}) + i*sin({1}))'
          .format(round(r*exp, 2), round(fi*exp, 2), exp))


def main():
    # num = a + bi.
    num = input('Enter complex number. For example, 12 + 2i:')
    exp = int(input('Enter exponent:'))

    a = re(num)
    b = im(num)

    # Module.
    r = mod(a, b)

    # Argument.
    fi = arg(a, b)

    trig(r, fi)
    power(r, fi, exp)


if __name__ == '__main__':
    main()
