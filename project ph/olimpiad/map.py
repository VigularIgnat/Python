#function map

number=int(input("Enter num"))
list1=list(map(int, input().split( ) ))
print(list1)
print(list1.index(max(list1))+1)
