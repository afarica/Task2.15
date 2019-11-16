# Write the code, which will print numbers from 0 till your age. And if your age
# is odd, will be printed all odd numbers till your age, if even all even numbers.
a=int(input("How old are you:"))
print(list(range(0,a+1)))
if a%2==0: 
	print(list(range(0,a+1,2)))	
elif a%2!=0:
	print(list(range(1,a+1,2)))
