accounts={
    101:["user1","user1@gmail.com",1234,3000,None],
    102:["user2","user2@gmail.com",2345,2200,5000],
    103:["user3","user3@gmail.com",3456,1000,None],
    104:["user4","user4@gmail.com",None,3500,None]
    }
print(accounts)

while True:
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Mini statement")
    print("4. Pin generation")
    print("5. Pin change")
    print("6. Loan details")
    print("7. Exit")
    choose=int(input("Enter your option:"))
    if choose==1:
        acc=int(input("Enter account number:"))
        if acc not in accounts:
            print("Invalid account number")
            print("---------------------------")
        else:
            if accounts[acc][2] is None:
                print("Pin is not generated")
                print("---------------------------")
            else:
                pin=int(input("Enter your pin:"))
                if accounts[acc][2]==pin:
                    amt=int(input("Enter amount:"))
                    if amt > accounts[acc][3]:
                        print("Insuffiencent balance")
                        print("---------------------------")
                    else:
                        print("Withdrawn successfully")
                        print("---------------------------")

    elif choose==2:
        acc=int(input("Enter account number:"))
        if acc not in accounts:
            print("Invalid account number")
        else:
            if accounts[acc][2] is None:
                print("Pin is not generated")
                print("---------------------------")
            else:
                pin=int(input("Enter your pin:"))
                if accounts[acc][2]==pin:
                    amt=int(input("Enter amount:"))
                    accounts[acc][3]+=amt
                    print(accounts[acc])
                    print("---------------------------")
    elif choose==3:
        acc=int(input("Enter account number:"))
        if acc not in accounts:
            print("Invalid account number")
            print("---------------------------")
        else:
            if accounts[acc][2] is None:
                print("Pin is not generated")
                print("---------------------------")
            else:
                pin=int(input("Enter your pin:"))
                if accounts[acc][2]==pin:
                    print("Name:",accounts[acc][0])
                    print("Email:",accounts[acc][1])
                    print("Balance:",accounts[acc][3])
                    print("---------------------------")
    elif choose==4:
        acc=int(input("Enter account number:"))
        if acc not in accounts:
            print("Invalid account number")
            print("---------------------------")
        else:
            if accounts[acc][2] is not None:
                print("Pin is already generated")
                print("---------------------------")
            else:
                while True:
                    pin=int(input("Enter your pin:"))
                    pin1=int(input("Re-enter the same pin:"))
                    if pin != pin1:
                        print("Enter same pin")
                        continue
                    else:
                        print("Pin generated successfully")
                        print("---------------------------")
                    break
    elif choose==5:
        acc=int(input("Enter account number:"))
        if acc not in accounts:
            print("Invalid account number")
            print("---------------------------")
        else:
            if accounts[acc][2] is None:
                print("Pin is not generated")
                print("---------------------------")
            else:
                while True:
                    pin=int(input("Enter previous pin:"))
                    if pin != accounts[acc][2]:
                        print("Enter correct previous pin")
                        continue
                    else:
                        pin1=int(input("Enter new pin:"))
                        accounts[acc][2]=pin1
                        print("New pin is updated")
                        print(accounts[acc])
                        print("---------------------------")
                        break
    elif choose==6:
        acc=int(input("Enter account number:"))
        if acc not in accounts:
            print("Invalid account number")
            print("---------------------------")
        else:
            if accounts[acc][4] is None:
                print("You are not having any loans")
                print("---------------------------")
            else:
                print(f"you are having {accounts[acc][4]} of loan amount")
                print("---------------------------")
    else:
        print("Thank You")
        print("Visit Again")
        print("---------------------------")
