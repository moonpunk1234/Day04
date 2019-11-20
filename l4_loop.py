#Python for Loop
#====================================		
#Syntax of for Loop

#for val in sequence:
	#Body of for

#The range() function
#We can generate a sequence of numbers using range() function. range(10) 
#will generate numbers from 0 to 9 (10 numbers).

numbers = list(range(10))
print(numbers)
print(list(range(1,6)))
print(list(range(5,20,3)))

#min(digits)
#max(digits)
#sum(digits)
#len(digits)

val = list(range(5,20))
print(min(val))
print(max(val))
print(sum(val))
print(list(range(5,20)))
print(len(val))

#Slicing a List
#numbers[start:end]

print(val[2:4])
print(val[2:])
print(val[:4])
print(val[:])
print(val[-1])
print(val[-7])

for x in [3,1,8,2]:
	print(x)
	
for x in range(20):
	print(x,end=' ')

print('\n')
print(50*'*')
for x in range(1,11):
	print(x,end=' ')

print('\n')
print(50*'*')
for x in range(1,100):
	print(x,end='\t')
	
mylist =['Apple','Banana','Mango','Pine Apple','Chand','Moon']
print(mylist[0])

for i in mylist:
	print(i,end='\t')
	
print('\n')
print(50*'*')	
fruits = []
for i in range(5):
	y = input('Enter some fruit : ')
	fruits.append(y)
	


for i in sorted(fruits):
	print(i,end='\t')	

print('\n')
print(50*'*')	

for i in fruits:
	print(i,end='\t')	
	



