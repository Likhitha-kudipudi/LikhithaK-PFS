'''
Handling errors :


try block:
> The try block will test a block of code for errors.
    try:
    print(b)
    
    except block :
    >This block will take care of any errors
        except:
        print("This block can handle error")

    
else block :

this else keyword to define a block of code to be executed if no error were 
finally block



try :
    a = 1
    b = 3
    print(a+b)
except :
    print("error")
else :
    print("no error")


 

++
try :
    a = 7888
    b = 8589
    print(a+b)
except :
    print("error")
else :
    print("no error")
finally:
    print("try except block is finished")
    


try :
    num = int(input("enter num:"))
    num2 = int(input("enter num2:"))
    result = num/num2
except ValueError:
    print("enter valid num")
except ZeroDivisionError :
    print("cannot divide")
else :
    print(f"result = {result}")
finally :
    print("completed")


try :
    num = int(input("enter num:"))
    num2 = int(input("enter num2:"))
    result = num/num2
    print(twice)
except NameError:
    print("not defined")
except ValueError:
    print("enter valid num")
except ZeroDivisionError :
    print("cannot divide")
else :
    print(f"result = {result}")
finally :
    print("completed")
'''


















    


