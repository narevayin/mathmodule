''' factorial '''
def factorial(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res

''' square root'''
def sqrt(x):
    res = x ** 0.5
    return res
print (sqrt(121))
'''logarithm'''

# x = 8
# base = 2
# y = 1
# while x != base ** y:
#     y += 0.01
#     continue

# else:
#     print(y)
    


''' radian to degree'''
def degrees(x):
    deg = x * 180 / 3.14159265359
    return deg

print (degrees(50))


''' absolute '''
def absolute(x, y):
    if x >= 0 and y >= 0:
        return x + y
    elif x < 0 and y > 0:
        x = x * -1
        return x + y
    elif x > 0 and y < 0:
        y = y * -1
        return x + y
    elif x < 0 and y < 0:
        y = y * -1
        x = x * -1
        return x + y


'''exponential of x'''
def exp(x):
    return x * 2.71828

'''power of'''
def pow(x, y):
    return x ** y

'''floor'''
def floor(x):
    return int(x // 1)


'''ceil'''

def ceil(x):
    return int((-1 * x // 1 * -1))


