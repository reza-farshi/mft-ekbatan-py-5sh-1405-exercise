#username and password

print("\n wellcome to my program \n")

main_username = "dark shadow"
main_password = "king arthor 7300"
user_age = 0

user_birth = int(input("please enter your year of birth :\n"))


if 1900 < user_birth < 2026 :

    user_age = 2026-user_birth

    print("your age is :",user_age)

elif 1300 <user_birth < 1405 :

    user_age = 1405-user_birth

    print("your age is :",user_age)

else :
    print("the entered date does not exist or YOU ARE DEAD")

if user_age < 18 :

    print("im'sorry BYE")

else :
    user_username = input("please enter username :")
    user_password = input("please enter password :")

    if user_username == main_username and user_password == main_password :

        print("login")
    
    elif user_username != main_username and user_password == main_password :

        print("username incorrect")

    elif user_password != main_password and user_username == main_username :

        print("password incorrect")

    else :

        print("username and password incorrect")