import random

computer =random.choice([-1,0,1])

you=input("Enter r For Rock,p for paper,s for Sissore:")

youDict={"r":-1,"p":0,"s":1}
reversDict={-1:"Rock",0:"Paper",1:"Sissore"}

if you not in youDict:
    print("Invalid value")

else:
    youNUM=youDict[you]

    print("Your chosse is",reversDict[youNUM])
    print("Computer chosse is",reversDict[computer])

    if computer==youNUM:
        print("It\'s a draw")

    elif (computer==1 and youNUM==0)or(computer==0 and youNUM==1)or(computer==1 and youNUM==-1):
        print("You Win..")
    else:
        print("You lost..")