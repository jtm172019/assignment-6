###### this is the first .py file ###########

####### write your code here ##########

print("Enter binary data to be transmitted")

#taking input of binary data to be transmitted
n=raw_input("Enter data:")
count=0
count1=0
index=0

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
#print l1
#for i in range(0,l1):
#	if msg_parity[i:i+2]=='010':
#		count1=count1+1
#print count1


string='010'
for i in range(0,l1):
	if msg_parity[i:i+3]==string:
		index=i+3
#adding 0 after 010
	msg1_parity=msg_parity[:index]+'0'+msg_parity[index+1:]
#print msg1_parity

#to add 0 if the frame ends with 01
string1='01'
if msg_parity[l1-2:]==string1:
	msg2_parity=msg1_parity[:len(msg1_parity)]+'0'
print msg2_parity

#Adding flag 0101 at the end of frame

final_string=msg2_parity[:len(msg2_parity)]+'0101'

print final_string






