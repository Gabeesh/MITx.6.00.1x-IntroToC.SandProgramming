def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    i = start
    sum = 0
    while i<stop:
        sum = sum + (f(i)*step)
        i = i + step
    return sum



print radiationExposure(40, 100, 1.5)