foods = []
prices = [] 
total = 0 


while True:
    food = input(f"enter the food you want later press q for quit  ")
    food.lower()
    if food == "q" : 
        print(f"-------items on cart -------------\n{foods}")
        print(f"with the total price of : {total:02}$")
        break 
    else : 
        print (f"u have choose {food} :/n  what else do you want ?") # 
        foods.append(food)
        price = int( input (f"enter the prize of the item choosen : $ "))
        prices.append(price)
        print(f"{(foods)}")
        print(f"{prices}")
        total = sum(prices)




    
        