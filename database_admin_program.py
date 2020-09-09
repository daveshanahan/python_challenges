log_on_info = {
    "davids1":"MahonAbtr!n1",
    "lydiam2":"Password1234",
    "carlynnH":"scheduling54321",
    "maryMcN":"Forecaster123",
    "colinM":"paymentsG145",
    "admin00":"administrator5",
}

print("Welcome to the database admin program")

username = input("\nPlease enter your username: ").strip()

# logic for control flow
if username in log_on_info:
    password = input("Please enter your password: ").strip()
    if password in log_on_info[username]:
        print("\nHello " + username + "! You are logged in")
        # if admin logs in
        if username == "admin00":
            print("Here is the current database:\n")
            for keys, values in log_on_info.items():
                    print("Username: " + keys + "\t\tPassword: " + values)
        else:
            # if other user logged in
            change_choice = input("Would you like to change your password: ").lower()
            if change_choice.startswith("y"):
                new_password = input("What would you like to change your password to: ")
                # check password length and add to dict if correct length
                if len(new_password) >= 8:
                    log_on_info[username] = new_password
                    print("\n" + username + ", your new password is " + new_password)
                # else reject password and display original
                elif len(new_password) < 8:
                    print(new_password + " is not the minimum password length of 8 characters.")
                    print("\n" + username + ", your password is " + password)
            elif change_choice.startswith("n"):
                print("Ok. Thank you for using the database admin program.")
    else:
        print("Password incorrect!")
else:
    print("Username not found. Goodbye!")


