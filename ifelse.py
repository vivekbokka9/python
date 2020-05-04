## if statement
## if condition to test:
##  code to execute if test passes

bank_balance = 50
item_cost = 60
item_inventory = 1
if item_cost < bank_balance and item_inventory >= 1:
    bank_balance -= item_cost
    print("transaction successful")
    print(bank_balance)
elif item_cost == bank_balance and item_inventory >= 1:
    ## a= a-b can be written as a -= b
    bank_balance -= item_cost
    print("Transaction Sucessful. But, no funds left")
    print(bank_balance)
else:
    if item_inventory < 1:
        print("not enough inventory")
    else:
        print("Transaction Failed, Insufficent Funds")
        print(bank_balance)