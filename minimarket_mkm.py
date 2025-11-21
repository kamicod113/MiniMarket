import time
import os
import json

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

user_file = 'users.json'
product_file = 'products.json'

script_dir = os.path.dirname(os.path.abspath(__file__))

product_path = os.path.join(script_dir, product_file)
with open(product_path, 'r', encoding = 'utf-8-sig') as file:
    categories = json.load(file)

users_path = os.path.join(script_dir, user_file)
with open(users_path, 'r', encoding ="utf-8-sig") as file:
    users = json.load(file)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print("\n>>>Welcome to MKM ShoppingWeb!!!<<<")

tries = 3
found = False
while tries > 0 and not found:
     enteredusername = input("Please enter your username: ")
     enteredpassword = input("Please enter your password: ")

     for user in users:
        if user["username"] == enteredusername and user["password"] == enteredpassword:
            found = True
            break
            
     if found:
        print("Login successful!")

        balance = user["balance"]
        username = user["username"]
        userpassword = user["password"]

#=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-- 
#     
        basket_file = f"{username}_basket.json"
        
        if not os.path.exists(basket_file):
            with open(basket_file, "w") as f:
                json.dump([], f)
        with open(basket_file, "r") as file:
            basket = json.load(file)

#=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-

        favorite_file = f"{username}_favorites.json"

        if not os.path.exists(favorite_file):
            with open(favorite_file, "w") as f:
                json.dump([], f)  
        with open(favorite_file, "r") as file:
            favorites = json.load(file)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        history_file = f"{username}_history.log" 

        if not os.path.exists(history_file):
            f = open(history_file, "w", encoding="utf-8")
            f.write("") 
            f.close 

#=-=-=-=--=-=-=-=-=-=-==-=-=-=-=--=-=-=-=-=-=-=-=-=-

        purchases_file = f"{username}_purchases.json"

        if not os.path.exists(purchases_file):
            with open(purchases_file, "w") as f:
                json.dump([], f)
        with open(purchases_file, "r") as file:
            purchases = json.load(file)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-

        while True:
                print("---------------------------------------------------------")
                print("1--> Catagories")
                print("2--> Basket")
                print("3--> Favorites")
                print("4--> History")
                print("5--> Settings")
                print("6--> Show my balance")
                print("7--> Exit")
                print("8--> Removing from basket or Favorites")
                print("9--> Shopping")
                print("10--> Increase balance") #bonus
                print("11--> Purchases ") #bonus
                print("---------------------------------------------------------")

                selectednumber = input("Select a number among - 1 2 3 4 5 6 7 8 9 10:  ")
                if selectednumber == "1": #sintaksis sehvi  var duzeld

                    print("=-=-=-=-=-CATEGORIES-=-=-=-=-=")                  
                    category_list = list(categories.keys())
                    for i, category in enumerate(category_list):
                     print(f"{i+1}. {category}")
                    categoryID = int(input("Choose the category id you want: "))
                    category_name = category_list[categoryID - 1]                   
                    items = categories[category_name]

                    print("=-=-=-=-=-PRODUCTS-=-=-=-=-=")
                    for item in items:
                        print(f"{item['id']}. {item['name']} - {item['price']} AZN")
                    choosenId = int(input("Choose the product id you want: "))
                    quantity = int(input("Enter the quantity you want: "))
                    action = input("If you want to add to favorites choose - F \n If you want to add to basket choose - B \n If you want cancel choose - X: ").upper()

                    for item in items:
                        if item["id"] == choosenId:
                                if action == "B":
                                    basket.append({
                                        "category": category_name,
                                        "name": item["name"],
                                        "price": item["price"],
                                        "quantity": quantity,
                                        "linetotal": quantity * item["price"] 
                                    })
                                    print("Product added succesfully")
                                    print("Your basket: ", basket)

                                    f = open(history_file, "a", encoding="utf-8")
                                    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Basket add - {item['name']} - {item['price']} \n")
                                    f.close

                                    f = open(basket_file, "w", encoding="utf-8")
                                    json.dump(basket, f, indent = 2)
                                    f.close()
                                    break

                                elif action == "F":
                                     favorites.append({
                                        "category": category_name,
                                        "name": item["name"],
                                        "price": item["price"]  
                                     })
                                     print("Product added succesfully")
                                     print("All your favorites: ", favorites)

                                     f = open(history_file, "a", encoding="utf-8")
                                     f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Favorite add - {item['name']} - {item['price']} \n ")
                                     f.close()

                                    
                                     f = open(favorite_file, "w", encoding = "utf-8")
                                     json.dump(favorites, f, indent = 2)
                                     f.close()
                                     break  
                                  
                                elif action == "X":
                                    print("Item Cancelled!")
                                    break               
                        else: 
                            print("The ID you selected is invalid. Please enter the correct ID.")

                elif selectednumber == "2": #isleyir amma professional yazmaq olar
                    print("=-=-=-=-=-BASKET-=-=-=-=-=")
                    print("Your basket: ", basket)
            
                elif selectednumber == "3": #isleyir prof yazmaq lazim
                    print("=-=-=-=-=-FAVORITES-=-=-=-=-=")
                    print("All your favorites: ", favorites)
                   
                elif selectednumber == "4": #islemelidi

                    f = open(history_file, "r", encoding="utf-8")
                    lines = f.readlines()
                    f.close()

                    if len(lines) == 0:
                        print("No History yet.")
                    else:          
                        n = int(input("How many recent transactions do you want to see? ")) 
                        print("=-=-=-=-=- HISTORY -=-=-=-=-=") 
                        if n > len(lines):
                            n = len(lines)
                        for line in lines[-n:]:
                                print(line.strip()) 

                elif selectednumber == "5": #tam duzgun isleyir 🥳🥳
                    print("=-=-=-=-=-CHANGING PASSWORD-=-=-=-=-=")
                    testpassword = input("Enter your password: ")

                    if testpassword == userpassword:
                        print("Warning!")
                        print("Password must be different from the previous password and must be min 4 digit")
                        newpassword = input("Enter your new password: ")

                        if newpassword != userpassword and len(newpassword) >= 4:
                            newpassword2 = input("Enter your new password again: ")

                            if newpassword == newpassword2:
                                user["password"] = newpassword

                                f = open(users_path, "w", encoding="utf-8-sig")
                                json.dump(users, f, indent=2)
                                f.close()

                                print("Password successfully changed!")

                                f = open(history_file, "a", encoding="utf-8")
                                f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Password change \n ")
                                f.close()

                            elif newpassword != newpassword2:
                                    print("Your passwords is not the same")
                        else:
                            print("Enter correct password!")
                    else:
                        print("Your password is incorrect")

                elif selectednumber == "6": #buda isleyir
                    print("=-=-=-=-=-BALANCE-=-=-=-=-=")
                    print("Your balance: ", balance)

                    f = open(history_file, "a", encoding="utf-8")
                    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Showing balance - Your balance is - {balance} AZN. \n ")
                    f.close()
                  
                elif selectednumber == "7": #buda isleyir
                    print("=-=-=-=-=-EXIT-=-=-=-=-=")
                    print("Goodbye. Your exit is succesfull")

                    f = open(history_file, "a", encoding="utf-8")
                    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Exit \n ")
                    f.close()
                    break

                elif selectednumber == "8": #yeqinki isleyir
                    print("If you want delete item from Basket select 1")
                    print("If you want delete item from Favorites select 2 ")

                    deletingelementnumber = input("Choose one of this; 1 or 2: ")
                    if deletingelementnumber == "1":
                        print("=-=-=-=-=-BASKET-=-=-=-=-=")
                        for item in basket:
                            print(f"{item['name']} x{item['quantity']}")

                        removed_name = input("Enter the product name you want remove: ")
                        found = False
                        for item in basket:
                            if item["name"].lower() == removed_name.lower():
                                basket.remove(item)
                                found = True
                                print("Updated Basket: ")
                                print(basket)
                                break

                        if not found:
                            print("This item is not in basket.") 

                        f = open(basket_file, "w", encoding="utf-8")
                        json.dump(basket, f, indent=2)
                        f.close()

                        f = open(history_file, "a", encoding="utf-8")
                        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Basket remove - {removed_name} \n ")
                        f.close()

                    elif deletingelementnumber == "2":
                        print("=-=-=-=-=-FAVORITES-=-=-=-=-=")
                        for item in favorites:
                            print(item["name"])

                        removed_name = input("Enter the product name you want remove: ")
                        found = False
                        for item in favorites:
                            if item["name"].lower() == removed_name.lower():
                                favorites.remove(item)
                                found = True
                                print("Updated Favorites:", favorites)
                                break

                        if not found:
                            print("This item is not in favorites.")

                            f = open(favorite_file, "w", encoding="utf-8")
                            json.dump(favorites, f, indent=2)
                            f.close()

                            f = open(history_file, "a", encoding="utf-8")
                            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Favorite remove - {removed_name} \n")
                            f.close()

                elif selectednumber == "9":
                    print("=-=-=-=-=-SHOPPING-=-=-=-=-=")
                    purchaseitem = input("Do you want buy all the items in basket?(Yes or No): ")
                    if purchaseitem.lower() == "yes":
                            confirm = input("Are you sure?(Yes or No): ")
                            if confirm.lower() == "yes":
                                if len(basket) == 0:
                                    print("Your basket is empty.")
                                else:
                                    amountbasket = sum(item["linetotal"] for item in basket)
                                    if balance >= amountbasket:
                                     balance -= amountbasket
                                     user["balance"] = balance
                                     print("Purchase successful!")
                                     print("Your new balance:", balance)

                                     for item in basket:
                                        purchases.append({
                                            "category": item["category"],
                                            "name": item["name"],
                                            "price": item["price"],
                                            "quantity": item["quantity"],
                                            "linetotal": item["linetotal"],
                                            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                                        })

                                     f = open(purchases_file, "w", encoding="utf-8")
                                     json.dump(purchases, f, indent=2)
                                     f.close()

                                     basket.clear()

                                     f = open(users_path, "w", encoding="utf-8-sig")
                                     json.dump(users, f, indent=2)
                                     f.close()

                                     f = open(basket_file, "w", encoding="utf-8")
                                     json.dump(basket, f, indent=2)
                                     f.close()

                                     f = open(history_file, "a", encoding="utf-8")
                                     f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Checkout - Total: {amountbasket} AZN \n ")
                                     f.close()

                                    else:
                                        print("Insufficient balance!")
                            elif confirm.lower()=="no":
                                print("Purchase cancelled")
                    elif purchaseitem.lower()=="no":
                        print("Purchase cancelled.")

                elif selectednumber == "10":
                    increasingamount = input("Write the amount you want to add: ")
                    if float(increasingamount) != increasingamount:
                        print("You must enter only number : bill and coin ")
                    else:
                        user["balance"] = balance 
                        print("Balance increased succesfully")
                        print("Your balance: " , balance)

                        f = open(users_path, "w", encoding="utf-8-sig")
                        json.dump(users, f, indent=2)
                        f.close()

                        f = open(history_file, "a", encoding="utf-8")
                        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Increase Balance - Amount: {balance} AZN \n ")
                        f.close()

                elif selectednumber == "11":
                    print("Your purchases:", purchases)

        break 
     
     else:
        tries -= 1
        print("Password or username is incorrect. You have", tries, "tries left.")

        if tries == 0:
            print("Your account was blocked for 10 seconds. Be patient and carefull")
            for i in range (10, 0, -1):
                print(f"{i} seconds remaining ...")
                time.sleep(1)
            tries = 3
            print("You can try again now.")