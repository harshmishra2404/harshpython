Email = input("Enter your Email-ID:")
Password = input("Enter the password:")
if '@' in Email:
    if Email == "harshm2404@gmail.com" and Password == "8355":
        print("welcome")
    elif Email == "harshm2404@gmail.com" and Password != "8355":
        print("Incorrect Password")
        Password = input("Enter correct Password:")
        if Password == "8355":
            print("Welcome")
        else:
            print("Still Incorrect")
            Password = input("Enter correct Password:")
    elif Email != "harshm2404@gmail.com" and Password == "8355":
        print("Incorrect Email-ID")
        Email = input("Enter correct Email-ID:")
        if Email == "harshm2404@gmail.com":
            print("Welcome")
        else:
            print("Still Incorrect")
            Email = input("Enter correct Email-ID:")
else:
    print("the format of Email-ID is wrong")
    Email = input("Enter correct Email-ID:")
    if Email == "harshm2404@gmail.com":
        print("Welcome")
    else:
        print("Still Incorrect")
        Email = input("Enter correct Email-ID:")