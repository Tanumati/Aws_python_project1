'''
# store datatype as list start index from 0
mylist = [3,14,5,6,8,4,3,2,2,]
mylist1= [5,98,6,7,]
#add value at the last index in list
mylist.append(5)
# insert value '1' in index no [7]
mylist.insert(7,1)
# remove value '14' 
mylist.remove(14)
# value remove in specific index number
mylist.pop(3)
# if you remove value with known index use list[i]
mylist1.remove(mylist1[1])
# clear command reomve all index value 
# mylist.clear()
# print index[2] value 
print(mylist)
print(mylist.index(4))
# print number of times x appers in the list
print(mylist.count(4))
# sort the item of the list inplace
print(mylist.sort())
# reverse the elments of the list in place
print(mylist.reverse())
# return ashallow copy of the list
print(mylist.copy())



#print(mylist[5])
#print(mylist)


#print(mylist[1])
'''



# warm up task2 
mylist = []
while len(mylist)<8:
  x= input("Do you want add a number to your list - enter 'y' or 'n'")

  if x == 'y':
     num = input("Enter the number")
     mylist.append(num)
  elif x == 'n':
      print(mylist)
      break
  else:
     print("invalid input")


   