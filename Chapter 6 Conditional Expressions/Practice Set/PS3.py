#Spam Keywords

P1="Subscribe Here"
P2="Click Here"
P3="Buy now"
P4="Make A Lot of Money"

message = input("Enter Your comment")

if(P1 in message or P2 in message or P3 in message or P4 in message ):
    print("Its is a SCAM!!")

else:
    print("You are SAFE")
