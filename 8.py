#dastgahe foroshe bilite cinema

print("\n wellcome to my program \n")

ticket = 200000
final_ticket = 0

age = int(input("please enter your age : "))

day = input("\n pelase enter the day \n 1.saturday \n 2.sunday \n 3.monday \n 4.tuesday \n 5.wednsday \n 6.thursday \n 7.friday\n")

if 0 < age < 12 :

    final_ticket = ticket * 0.5

    print("your ticket price is",final_ticket,"toman")


elif 60 < age < 100 :

    final_ticket = ticket * 0.7

    print("your ticket price is",final_ticket,"toman")

elif 12 < age < 60 :

    if day == "4" or day =="tuesday" :

        final_ticket = ticket * 0.8

        print("your ticket price is",final_ticket,"toman")
    else :

        print("your ticket price is",ticket,"toman")

else :
    
    print("you are DEAD")