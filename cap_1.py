print "Problem 1: Open a new Python interpreter and use it to find the value of 2 + 3."

print (2 + 3)

print "-"*30

print "Problem 2: Create a python script to print hello, world! four times."
for _ in range(4):
    print 'hello, world!'

print "-"*30

print "Problem 4: What will be output of the following program."
"""
    x = 4
    y = x + 1
    x = 2
    print x, y
"""

def prob_4():
    x = 4
    y = x + 1
    x = 2
    print x, y

prob_4()

print "-"*30

print "Problem 5: What will be the output of the following program."
"""
    x, y = 2, 6
    x, y = y, x + 2
    print x, y # 6, 4
"""

def prob_5():
    x, y = 2, 6
    x, y = y, x + 2
    print x, y

prob_5()

print "-"*30

print "Problem 6: What will be the output of the following program."

"""
    a, b = 2, 3
    c, b = a, c + 1
    print a, b, c # error
"""

def prob_6():
    c = 0 # comment it to see error # 2, 1, 2
    a, b = 2, 3
    c, b = a, c + 1
    print a, b, c # error

prob_6()

print "-"*30

print "Problem 7: How many multiplications are performed when each of the following lines of code is executed?"
"""
    print square(5)
    print square(2*5)
"""

def square(x):
    return x * x

def prob_7():
    print square(5)
    print square(2*5)

prob_7()


print "-"*30

print "Problem 8: What will be the output of the following program?"
"""x = 1
def f():
    return x
print x
print f()"""

x = 1
def f():
    return x
print x
print f()

print "-"*30

print "Problem 9: What will be the output of the following program?"
"""x = 1
def f():
    x = 2
    return x
print x
print f()
print x"""

x = 1
def f():
    x = 2
    return x
print x
print f()
print x

print "-"*30

print "Problem 10: What will be the output of the following program?"
""" x = 1
def f():
        y = x
        x = 2
        return x + y
print x
print f()
print x"""

x = 1
def f():
    x = 0 #comment it to see error -- error
    y = x
    x = 2
    return x + y
print x #1
print f() # 3
print x # 1

print "-"*30

print "Problem 11: What will be the output of the following program?"
"""x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print x, y
"""
x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print x, y #2, 9

print "-"*30

print "Use of lambda"
cube = lambda x: x ** 3
print cube(3)

print "-"*30

print "Problem 14: What will be output of the following program?"
"""print 2 < 3 and 3 > 1
print 2 < 3 or 3 > 1
print 2 < 3 or not 3 > 1
print 2 < 3 and not 3 > 1"""

print 2 < 3 and 3 > 1 #  True
print 2 < 3 or 3 > 1 # True
print 2 < 3 or not 3 > 1 # True
print 2 < 3 and not 3 > 1 # False
print "-"*30

print "Problem 15: What will be output of the following program?"
"""x = 4
y = 5
p = x < y or x < z
print p"""

x = 4
y = 5
p = x < y or x < z
print p #TRue
print "-"*30

print "Problem 16: What will be output of the following program?"

True, False = False, True
print True, False
print 2 < 3
print "-"*30

print "Problem 17: What happens when the following code is executed? Will it give any error? Explain the reasons."
"""x = 2
if x == 2:
    print x
else:
    print y"""

x = 2
if x == 2:
    print x
else:
    print yy

# Note: will error only when else block gets exicuted

print "-"*30

print "Problem 18: What happens the following code is executed? Will it give any error? Explain the reasons."
"""x = 2
if x == 2:
    print x
else:
    x + #syntax error here
"""

x = 2
if x == 2:
    print x
else:
    x + 0 #remove 0 to show error
print "-"*30

print "Modules"
import time
print time.asctime()