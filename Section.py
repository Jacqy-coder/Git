# fruits= ["range","pear", "banana","grapes"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[-1])
# #indexing
# print(fruits.index('range'))
# print(fruits.index('grapes'))
#
# fruits=("ange","pear", "banana","grapes")
# print(fruits)
# dic = {"name": "anthony", "age": 27, "shop": "rice"}
# print("the age of anthony is:", dic['age'])
# dic['age'] = 44
# dic['shop'] = 'soap'+'rice'
# print(dic)
#
#
# print(dic) #adding items in a dic
# dic = {"name": "anthony", "age": 27, "shop": "rice"}
# dic["travel"] = "masai mara"
# #print(dic)
# for key, value in dic.items():
#     print("{} is {}".format(key, value))
# #dictionary has keys and values

#write a file in python
# f= open("section.txt", "w")
# f.write("hello class\n")
# f.writelines("This is a pyton class")
#read data in a .txt file
# f=open("section.txt", "r")
# print(f.readlines())
# f.seek(0)
# print(f.read(10))
#append text in file
header = "Write data"
f= open("section.txt", "a")
f.write("This is an added text\n")
f.close()

# f= open("section.txt", "a")
#
# f.write("TODAY\n")
# f.close()

print("this is git information")