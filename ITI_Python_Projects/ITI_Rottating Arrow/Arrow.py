import os
import time
n=int(input("Enter the height of the arrows : "))
while(1):
	
	for i in range(n):#arrow Pointing Toward's UPWARDS
		for j in range(i,n):
			print(" ",end=" ")
		for j in range(i):
			print("*",end=" ")
		for j in range(i+1):
			print("*",end=" ")
		print() 
	for i in range(n):
		print(n*"  ",end="*\n")
	

		
	time.sleep(1)
	os.system("cls")
	for i in range(n):	#arrow Pointing Toward's LEFT
		for j in range (n-i):
			print(" ",end=" ")
		for j in range(i):
			print("*",end=" ")
		print()
	for i in range(n):
		if(i==0):
			print(2*(n)*"* ",end="")
		if(i!=0):
			for j in range (i):
				print(" ",end=" ")
			for j in range(n-i):
				print("*",end=" ")
		print()
	time.sleep(1)
	os.system("cls")
	
	for i in range(n):#arrow Pointing Toward's Downwards
		print(n*"  ",end="*\n")
	
	for i in range(n):
		for j in range(i+1):
			print(" ",end=" ")
		for j in range(i+1,n):
			print("*",end=" ")
		for j in range(i,n):
			print("*",end=" ")
		print() 
	
	time.sleep(1)
	os.system("cls")		
		
	# for i in range(n):
		# for j in range (i):
			# print("*",end=" ")
		# for j in range(n-i):
			# print(" ",end=" ")
		# print()
	# for i in range(n):
		# for j in range (n-i):
			# print("*",end=" ")
		# for j in range(n-i):
			# print(" ",end=" ")
		# print()
	for i in range(n):
		if i== n-1: 
			print((2*n)*"*", end="")
			print((i+1)* " * ")
		else:
			print((2*n)* " ", end ="")
			print((i+1)* " * ")
	for j in range(n-1,0,-1):
		print((2*n)* " ", end= "")
		print(j* " * ")



	time.sleep(1)
	os.system("cls")