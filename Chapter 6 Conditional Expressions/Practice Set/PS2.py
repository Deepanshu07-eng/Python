a=int(input("Enter Physics Marks: "))
b=int(input("Enter Chemistry Marks: "))
c=int(input("Enter Maths Marks: "))

# Check for total percentage



total_percentage = (100 *(a + b + c))/ 300
print(" your percentage is", total_percentage)

if(total_percentage >= 40 and a>=33 and b>=33 and c>=33):
    print("You are pass")
else:
    print("You Failed")