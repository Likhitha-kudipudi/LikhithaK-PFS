'''
List ---> Collection of different types inside the [] which are separated by ','
        [1,"name",[1,2,"likhi"]]

1)
list_1 = [1,2,3,"python",[1,2,["python","java"],"language"]]
print(list_1[4])
print(list_1[4][2])
print(list_1[4][2][0])
print(list_1[4][2][0][3])

2)
list_p = [2,6,"Likhitha",59,["stans",0,2],"TWICE"]
print(list_p[2])
print(list_p[4][0])
print(list_p[5])


Methods of Lists :
----------------
append()----->this method is used to add new items into list it will only go for the last index of the list

list_2 = [1,2,3,4,5]
print(list_2)
list_2.append(67)
print(list_2)
list_2.append([23,67])
print(list_2)

extend()-----> this method will add items into the list it will go in the last index ,where each item or sub string will be an index 

list_3 = [1,2,3,4,5]
print(list_3)
list_3.extend("LIKHITHA")
print(list_3)
list_3.extend("twice")
print(list_3)

remove()----->this method will remove/delete the item/value directly

list_4 = [1,2,3,4,"python",5]
print(list_4)
list_4.remove("python")
print(list_4)

pop()----->this method will delete the item/value based on the index

list_5 = [23,"python",56,89,6]
list_5.pop(1)
print(list_5)

MUTABLE                                                 IMMUTABLE
i can directly modify on that particular variable       i can not modify directly on the variable

'''





