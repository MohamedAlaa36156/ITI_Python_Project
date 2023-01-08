import os
import time
n=int(input("Enter the height of the arrows"))
while(1):
	
	for i in range(n):
		for j in range(i,n):
			print(" ",end=" ")
		for j in range(i):
			print("*",end=" ")
		for j in range(i+1):
			print("*",end=" ")
		print() 
	time.sleep(1)
	os.system("cls")
	for i in range(n):
		for j in range (n-i):
			print(" ",end=" ")
		for j in range(i):
			print("*",end=" ")
		print()
	for i in range(n):
		for j in range (i):
			print(" ",end=" ")
		for j in range(n-i):
			print("*",end=" ")
		print()
	time.sleep(1)
	os.system("cls")
	
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
		
	for i in range(n):
		for j in range (i):
			print("*",end=" ")
		for j in range(n-i):
			print(" ",end=" ")
		print()
	for i in range(n):
		for j in range (n-i):
			print("*",end=" ")
		for j in range(n-i):
			print(" ",end=" ")
		print()
	time.sleep(1)
	
		
	
	os.system("cls")