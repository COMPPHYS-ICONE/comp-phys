'''
>>> temp_conv(0)
32.0

>>> temp_conv(117)
242.6



'''



def temp_conv(c):
    f = (9.0/5)*c + 32
    return f


if __name__ == "__main__":
    import doctest
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type = float)
    args = parser.parse_args()
    c = args.c

    y = temp_conv(c)
    print c, 'degrees Celsius is', y,'degrees Fahrenheit'