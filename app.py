import random, time
login = 1
while (login <=3):
    print("WELCOME TO HACKERS WORLD")
    username =['hackersworld@21.com','pythondevelop@23.com']
    password = [8055,7016]
    print("--------------")
    u = input("enter your username:")
    p = int(input("enter your password:"))
    print()
    if u in username and p in password:
        print("OTP Generating....")
        print()
        time.sleep(3)
    else:
        print(login,"Attempt..Invalid Entry")
        print()
        if login == 3:
            print("your 3 attempts is over login again...")
        login +=1
        continue

    count = 1
    while (count<=3):
        otp = random.randrange(1000,9999)
        print(otp)
        num=int(input("enter OTP number:"))
        if num == otp:
            print("successfully login")
            print("your data is hacked")
            break
        else:
            print('invalid OTP...',count,'attempt')
            if count ==3:
                print('exceeded your login limit ')
            count +=1
    break

