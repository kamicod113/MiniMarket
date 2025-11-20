import time
print("Welcome to our ShoppingWeb!!!")
#sebetde umumi mebleg
a = 3
found = False
username = "Medina"
userpassword = "MedinA129"
balance = 500
category = [[0, "T-shirt" , 12.50 ] , [1,"Hoodie" , 45.00 ] , [2,"Jeans" , 50.00]]
categoryID = [0, 1, 2]
history = []
B=[] #sebete elave et
F=[] #favorilere elave et
while a > 0:
    enteredusername = input("Please enter your username:   ")
    enteredpassword = input("Please enter your password:  ")
    if userpassword == enteredpassword and username == enteredusername :
        while True:
            print("1-->Catagories")
            print("2-->Basket")
            print("3-->Favorites")
            print("4-->History")
            print("5-->Settings")
            print("6-->Show my balance")
            print("7-->Exit")
            print("8-->Removing from basket or Favorites")
            print("9-->Shopping")
            print("10-->Increase balance")#bonus
            print("---------------------------------------------------------")
            selectednumber = input("Select a number among: 1 2 3 4 5 6 7 8 ")
            if selectednumber == "1":
                history.append("1-->Catagories")
                print(category)
                choosenId = int(input("Choose the id you want: "))
                selectedcatagory = input("If you want to add to favorites choose : F\nIf you want to add to basket choose : B  ")
                if choosenId in categoryID:
                    for item in category:
                        if item[0] == choosenId:
                            if selectedcatagory.upper() == "B":
                                itemcount = int(input("How many products need to be added?: "))
                                B.append(item * itemcount)
                                print("Product added succesfully")
                                print("Your basket: ", B)
                                break
                            elif selectedcatagory.upper() =="F":
                                F.append(item)
                                print("Product added succesfully")
                                print("All your favorites: ", F)
                                break
                    else:
                        print("Id was not founded. Please choose the right Id")
                else:
                    print("Id was not founded. Please choose the right Id")
            elif selectednumber == "2":
                print("Your basket: ", B)
                history.append("Basket")
            elif selectednumber == "3":
                print("All your favorites: ", F)
                history.append("Favorites")
            elif selectednumber == "4":
                history.append("History")
                print(history)
            elif selectednumber=="5":
                history.append("Settings")
                testpassword=input("Enter your password: ")
                if testpassword==userpassword:
                    newpassword=input("Enter your new password: ")
                    if newpassword == userpassword:
                        print("Your new password must be different from the previous password")
                    elif len(newpassword)>4:
                        newpassword2=input("Enter your new password again: ")
                        if newpassword==newpassword2:
                            userpassword=newpassword
                            print("Password successfully changed!")

                        elif newpassword!=newpassword2:
                                print("Your passwords is not the same")
                    else:
                        print("Your passwords length must be greater than 4.")
                else:
                    print("Your password is incorrect")
            elif selectednumber == "6":
                print("Your balance: ", balance)
                history.append("Balance")
            elif selectednumber == "7":
                print("Goodbye Medina. Your exit is succesfull")
                history.append("Exit")
            elif selectednumber == "8":
                history.append("Removing item")
                print("If you want delete item from Basket select 1")
                print("If you want delete item from Favorites select 2 ")
                deletingelementnumber = input()
                if deletingelementnumber == "1":
                    print(B)
                    removedID =int(input("Choose the ID you want delete"))
                    if removedID in [item[0] for item in category]:
                        B = [item for item in B if item[0] != removedID]
                        print("Updated Basket:", B)
                    else:
                        print("Please enter the ID that exsist in category")
                if deletingelementnumber == "2":
                    print(F)
                    removedID = int(input("Choose the ID you want delete"))
                    if removedID in [item[0] for item in category]:
                        F = [item for item in F if item[0] != removedID]
                        print("Updated Favorites:", F)
                    else:
                        print("Please enter the ID that exsist in category")
            elif selectednumber=="9":
                history.append("Shopping")
                purchaseitem=input("Do you want buy all the items in basket?(Yes or No)")
                if purchaseitem.lower()=="yes":
                        confirm=input("Are you sure?(yes or no) ")
                        if confirm.lower()=="yes":
                            amountB= sum(item[2] for item in B)
                            if balance >= amountB:
                                balance -= amountB
                                print("Purchase successful!")
                                print("Your new balance:", balance)
                                B.clear()
                            else:
                                print("Insufficient balance!")
                        elif confirm.lower()=="no":
                            print("Purchase cancelled")
                elif purchaseitem.lower()=="no":
                    print("Purchase cancelled.")
            elif selectednumber == "10":
                history.append("Increasing balance")
                increasingamount = int(input("Write the amount you want to add: "))
                balance = balance + increasingamount
                print("Balance increased succesfully")
                print("Your balance: " , balance)
                    



    else:
        print("Password or username is incorrect. Please enter again. Don't forget you have only 3 chances")
        a=a-1
    
    if a == 0:
        print("Your account was blocked for 10 seconds be patient and carefull")
        time.sleep(10)