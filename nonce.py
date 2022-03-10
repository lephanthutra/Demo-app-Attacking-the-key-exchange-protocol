import random

# method that creates a random 10 bit number as a string to serve as our nonce
def nonceGenerator():
	num = ""
	for i in range(10):
		rand = random.randint(0,1)
		num += str(rand)
	return num

# # Alice'nonce
# NA = nonceGenerator()
# print("Alice's nonce is: ", NA)

# # Bob's nonce
# NB = nonceGenerator()
# print("Bob's nonce is:", NB)