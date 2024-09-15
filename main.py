#mpesa app

print(
    """
    mmmm   mmmm   pppppp   EEEEEEEEE    ssssss       AA
    mm mm mm mm  pp    pp  EE          ss          AA  AA
    mm  mm   mm  ppppppp   EEEEEEE      sssss     AAAAAAAA
    mm  mm   mm  pp        EE               ss   AA      AA 
    mm       mm  pp        EEEEEEEEE    sssss   AA        AA
    """
)

#common functions
def line():
    print("==============================================")

#this function prints a message when the user enters an option that does not appear in the list of options
def invalid():
    print("Invalid option selected")

#prints a message to the user incase the amount of money he/she wants to send
#/buy airtime/use lipa na mpesa is not enough for the transaction
def less(mpesaBalance):
    print(f"Insufficient funds in your mpesa. Your M-pesa balance is {mpesaBalance}.")

#this function prints a success message everytime the user withdraws money from his account
#workingAmount is the amount of money included in the transaction
#mpesaBalance - the amount of money still in yr mpesa account after the transaction has been processed
#transactionCost - amount of money paid for the transaction to be processed
def sucess(transactionCost, workingAmount, mpesaBalance):
    print(f"Transaction of {workingAmount} has been processed. The transaction cost was ksh {transactionCost}.Your new m-pesa balance is {mpesaBalance}")

#first allow the user to deposit some amount into the M-pesa
depositAmount = int(input("Deposit some money. > ksh "))

#global variables...
mpesaBalance = depositAmount
airtimeBalance = 0
mshwariBalance = 0
transactionCostLevelOne = 27 #this is the lowest transaction cost
transactionCostLevelTwo = 28 #this is the sec transaction cost
transactionCostLevelThree = 35  #this is the third transaction cost
transactionCostFour = 50  #this is the highest transaction cost


#use a loop to repeatedly run the code
while True:
    # allow the user to select options
    line()
    print("Select an option below.")
    print("1) Send Money")
    print("2) Withdraw cash")
    print("3) Buy airtime")
    print("4) Loans and savings")
    print("5) Lipa na Mpesa")
    print("6) My account")

    mPesaSelectedOption = input("> ")

    #check the option that has been selected by the user
    if mPesaSelectedOption == "1":
        print("Sending Money")
        #sening money to another user
        #second person phone number
        phone = input("Phone: > +254")
        #amount
        sendAmount = int(input("Amount: > ksh"))
        ##check if mpesa balance is more than the entered amount of money
        #coz the user can only send money only when his/her mpesa balance is more or equal
        #to the amount of money that the user want to send
        if sendAmount <= mpesaBalance:
            # proceed to send the amount
            #deduct the sent amount from the current mpesa balance
            mpesaBalance -= sendAmount #this is the new mpesa balance after the user has sent the money
            #print a success message and new mpesa balance
            print(f"QAF5767F confirmed you have sent ksh {sendAmount} to 0{phone}. Your new M-Pesa balance is ksh {mpesaBalance}.")
        else:
            less(mpesaBalance)

    elif mPesaSelectedOption == "2":
        print("Withdraw cash")
        #enter the amount that you wanna withdraw
        withdrawalAmount = int(input("> ksh "))

        #the user can only withdraw an amount lower than the M-pesa balance + the transaction cost
        #transaction cost varies with the amount of money that the user wants to withdraw
        totalCostLevelOne = transactionCostLevelOne + withdrawalAmount #this is the lowest transaction cost + withdrawal amount
        totalCostLevelTwo = transactionCostLevelTwo + withdrawalAmount #this is the sec transaction cost + withdrawal amount
        totalCostLevelThree = transactionCostLevelThree + withdrawalAmount #this is the third transaction cost + withdrawal amount
        totalCostLevelFour = transactionCostFour + withdrawalAmount #this is the highest transaction cost + withdrawal amount

        if withdrawalAmount < 999:
            #check if the mpesa balance is more or equal to totalCostLevelOne
            if totalCostLevelOne <= mpesaBalance:
                #deduct the withdrawn amount and transaction cost from  mpesa balance
                mpesaBalance -= totalCostLevelOne
                sucess(transactionCostLevelOne, withdrawalAmount, mpesaBalance)
            else:
                less(mpesaBalance)
        elif withdrawalAmount < 3000 and withdrawalAmount > 999:
            #check if the mpesa balance is more or equal to totalCostLevelOne
            if totalCostLevelTwo <= mpesaBalance:
                #deduct the withdrawn amount and transaction cost from  mpesa balance
                mpesaBalance -= totalCostLevelTwo
                sucess(totalCostLevelTwo, withdrawalAmount, mpesaBalance)
            else:
                less(mpesaBalance)
        elif withdrawalAmount < 5000 and withdrawalAmount > 3000:
            #check if the mpesa balance is more or equal to totalCostLevelOne
            if totalCostLevelThree <= mpesaBalance:
                #deduct the withdrawn amount and transaction cost from  mpesa balance
                mpesaBalance -= totalCostLevelThree
                sucess(totalCostLevelThree, withdrawalAmount, mpesaBalance)
            else:
                less(mpesaBalance)
        elif withdrawalAmount > 5000:
            #check if the mpesa balance is more or equal to totalCostLevelOne
            if totalCostLevelFour <= mpesaBalance:
                #deduct the withdrawn amount and transaction cost from  mpesa balance
                mpesaBalance -= totalCostLevelFour
                sucess(totalCostLevelFour, withdrawalAmount, mpesaBalance)
            else:
                less(mpesaBalance)

    elif mPesaSelectedOption == "3":
        print("Buy airtime")
        #when buying airtime transaction cost is 0
        airtimeAmount = int(input("Airtime amount: >"))

        if airtimeAmount > mpesaBalance:
            less(mpesaBalance)
        else:
            #buy airtime
            #deduct the airtime amount from mpesa balance
            mpesaBalance -= airtimeAmount
            #add the new airtime to airtime balance
            airtimeBalance += airtimeAmount
            print(f"You have purchased {airtimeAmount}. Your airtime balance is {airtimeBalance}. Your new mpesa balance is {mpesaBalance}")
    elif mPesaSelectedOption == "4":
        line()
        print("Loans and savings")
        print("1) Send to Mshwari")
        print("2) Withdraw from Mshwari")
        print("3) Check balance")
        mshwariSelectedOption = input("> ")
        if mshwariSelectedOption == "1":
            saveAmount = int(input("Enter amount you wanna send. > ksh "))
            if saveAmount > mpesaBalance:
                less(mpesaBalance)
            else:
                mpesaBalance -= saveAmount
                mshwariBalance += saveAmount
                print(f"You have saved {saveAmount} from your mpesa. Your new mshwari balance is {mshwariBalance} and mpesa balance is {mpesaBalance}")
        elif mshwariSelectedOption == "2":
            withDrawMshwariAmount = int(input("Enter amount you wanna withdraw. > ksh "))
            if withDrawMshwariAmount > mshwariBalance:
                less(mshwariBalance)
            else:
                mshwariBalance -= withDrawMshwariAmount
                mpesaBalance += withDrawMshwariAmount
                print(f"You have withdrawn {withDrawMshwariAmount} from your mshwari savings account. Your new mshwari balance is {mshwariBalance} and mpesa balance is {mpesaBalance}")
        elif mshwariSelectedOption == "3":
            print(f"Your Mshwari balance is {mshwariBalance}")
        else:
            invalid()

    elif mPesaSelectedOption == "5":
        print("Lipa na Mpesa")
        paybillNumber = int(input("Paybill:> "))
        accNumber = input("Account Number:> ")
        amount = int(input("Amount:> ksh"))
        if amount > mpesaBalance:
            less(mpesaBalance)
        else:
            mpesaBalance -= amount
            sucess(0, amount, mpesaBalance)
    elif mPesaSelectedOption == "6":
        print("My account")
        print(f"Mpesa Balance = {mpesaBalance}, airtime balance = {airtimeBalance} and mshwari acc balance = {mshwariBalance}")
    else:
        invalid()




