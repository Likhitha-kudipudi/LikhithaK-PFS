'''
Generator :
------------

>This is a special type of function that return an ITERATOR  which one at a time

def my_generator():
    yield 1
    yield 2
    yield 3
an = my_generator()
print(next(an))
print(next(an))
print(next(an))


def sare_gem(n) :
    for i in range(n) :
        yield i*i
for pal in sare_gem(5) :
    print(pal)

YIELD :
------
> It will take a pause and again resume , this is not a normal keyword can not be used in the normal functions.
>This is used to produce a value and pause execution.


def power_gen(o) :
    for i in range(o) :
        yield i +i
for hum in power_gen(10) :
    print(hum)

def power_gen(o) :
     for i in range(o) :
         yield i-i
for hum in power_gen(10) :
    print(hum)

def power_gen(o) :
    for i in range(o) :
        yield i/2
for hum in power_gen(10) :
    print(hum
NEXT :
-----
>when the value is finished , it will stop the iterator



#simple countdown:

def power_gen(o) :
     for i in range(o) :
         yield i
for hum in power_gen(30) :
    print(hum)


'''



















