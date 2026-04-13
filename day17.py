'''
Lambda function() :
--------------------
>This is also called ananymous function.
>A lambda function can take n number of arguments but have only one expression

syntax :
-------
>  lambda(keyword) arguments :expression

some = lambda an, how, do : (how - an)*do
print(some(4,9,2))


#multiplication
nayeon = lambda jeongyoung ,momo : momo *jeongyoung
print(nayeon(8,8))


#division
sana = lambda jihyo, mina : jihyo / mina
print(sana(8,7))


#substraction
dahyun = lambda chaeyoung,  tzuyu : chaeyoung - tzuyu
print(dahyun(3,7))


#addition
one_in_a_million = lambda Twice, once : Twice + once
print("Twice + Once < 3" ,one_in_a_million(9,1) )


List comprehension :
---------------------
>This offers the shorter syntax when want to create a new list from the existing list

syntax :
-------
>variable_name = [expression loop and condition]


old_list = [1,2,3,4,5]
new_list = [j for j in old_list if j % 2 ==0 ]
print(new_list)


'''


