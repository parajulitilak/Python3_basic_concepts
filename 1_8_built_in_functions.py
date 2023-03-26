print("Hi,my name is Tilak") #print function()
print(str(61)) #converting things into string
print(str(61.69)) #converting things to float
print(True) #boolean function

#converting things into integer and float
print(int('5'))
print(float("5.99"))

#string ,boolean testing
stri="True"
print(bool(stri)) #this line will print true

#len in string
print(len("My name is Tilak Parajuli")) #1 white space =1 and, 1 character=1
#output=25 ....in the above print function


#len in array
myarray=[1,2,3,4,5,6,7,8,9,1,1,5]
print(len(myarray))
#output=12

mynewlist=(["Hello","tilak","Parajuli"])
print(len(mynewlist))
#output=3

#sorting
print(sorted(myarray))
#output:[1, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

print(sorted(mynewlist)) #sorts capial to small
#output:['Hello', 'Parajuli', 'tilak']

print(sorted(["Hello","hello","5","A","a","5.56"]))
#output:['5', '5.56', 'A', 'Hello', 'a', 'hello']
