print("Welcome to the Shipping Accounts Program")

# set list of usernames and define prices
usernames = ["dshanahan", "lmccarthy", "charrison", "mmcnally", "cmurphy"]
price_0_100 = 5.10
price_100_500 = 5.00
price_500_1000 = 4.95
price_1000_plus = 4.80

# gather user input and welcome user back
user = input("Hello, what is your username? ")

# check for user account and welcome message
if user in usernames:
    print("\nHello " + user + ". Welcome back to your account.")
    print("Current shipping prices are as follows:")
    print("\nShipping orders 0 to 100:\t$" + format(price_0_100, ".2f") + "\nShipping orders 100 to 500:\t$" + format(price_100_500, ".2f") + "\nShipping orders 500 to 1000:\t$" + format(price_500_1000, ".2f") + "\nShipping orders over 1000:\t$" + format(price_1000_plus, ".2f"))

    # get user input for number of orders and calculate cost
    num_orders = int(input("\nHow many items would you like to ship: "))

    # logic to calculate cost
    if num_orders <= 100:
        print("\nTo ship " + str(num_orders) + " items it will cost you $" + format(num_orders*price_0_100, ".2f") + " at $" + format(price_0_100, ".2f") + " per item.")
        
    elif num_orders <= 500:
        print("\nTo ship " + str(num_orders) + " items it will cost you $" + format(num_orders*price_100_500, ".2f") + " at $" + format(price_100_500, ".2f") + " per item.")
 
    elif num_orders <= 1000:
        print("\nTo ship " + str(num_orders) + " items it will cost you $" + format(num_orders*price_500_1000, ".2f") + " at $" + format(price_500_1000, ".2f") + " per item.")

    else:
        print("\nTo ship " + str(num_orders) + " items it will cost you $" + format(num_orders*price_1000_plus, ".2f") + " at $" + format(price_1000_plus, ".2f") + " per item.")

    #confirm whether to send order or not
    decision = input("\nWould you like to place this order(y/n): ")
    if decision.startswith("y"):
        print("Okay. Shipping your " + str(num_orders) + " items.")
    else:
        print("Okay. No order is being placed at this time")

#if no account
else:
    print("Sorry, you do not have an account. Goodbye.")




