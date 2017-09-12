###### this is the first .py file ###########

####### write your code here ##########

print("Enter binary data to be transmitted")

#taking input of binary data to be transmitted
n=raw_input("Enter data:")
count=0
count1=0


#getting number of bits in data

l=len(n)

#finding number of 1's in data
for i in range(0,l):
	if n[i]=='1':
		count=count+1
#adding parity bit 
if count%2==0:
	msg_parity=n[:l]+'1'
else:
	msg_parity=n[:l]+'0'
print msg_parity

#checking message for 010 sequence
l1=len(msg_parity)
for i in range(0,l1):
	if msg_parity[i:i+2]=='010':
		count1=count1+1
print count1








