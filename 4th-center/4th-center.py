import random

def findchar(k): 
	#Generate a random integer to determine which array index to choose for evaluation.
	x = random.randint(0,200)
	print(k[x]) #shows the value of the index chosen
	#change the range to alter probabilities
	if 1<= k[x] <=100:
		return 'Hanamaru'
	elif 101<= k[x] <=700:
		return 'Yoshiko'
	else:
		return 'Ruby'

#initialization
k=[]

#integers in range 1-1000 will be generated for 200 times and inserted into array k
for x in range(200):
	k.append(random.randint(1,1001))

char = findchar(k)
print(char)
exit=input("press any key to exit") #so console doesn't close immediately