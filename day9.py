'''
j---> is a initial variable where it cannot show any error in the output ,that variable itself initialised where it can show anytime

a = 9
print(b)
for j in range(1,10):
    print(j)


range()---> This is used to generate number
syntax---> range(start(optional),end,optional)

 
for j in range(0,20,3):
    print(j)

any_ = "123"
print((list(any_)))
print(len(list(any_)))
print(tuple(any_))
print(int(any_))
print(float(any_))
print(str(any_))

a = [1,2,3]
v = str(a)
print(type(v))

l= [(1,2),(3,4)]
print(dict(l))
'''
'''
a = "TZUYU"
print(a[::-1])
emp = ""
for j in a:
    emp +=j
    emp = j +emp
    print(emp)

'''
reverse_str = "TWICE"
empty_ = ""
for j in reverse_str :
    empty_ = j + empty_
if empty_ == reverse_str :
    print(f"{reverse_str} is palindrome")
else :
    print(f"{reverse_str} is not PALINDROME ")

