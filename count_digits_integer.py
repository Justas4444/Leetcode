user_input=int(input("Enter number:"))
count=0
while(user_input>0):
    count=count+1
    user_input=user_input//10
print("The number of digits in the number are:",count)