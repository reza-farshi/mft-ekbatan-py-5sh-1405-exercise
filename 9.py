#sabte sefareshe resturant


print("\n wellcome to my program \n")
price = 0
pizza_price = 250000
burger_price = 180000
sandwich_price = 120000
coca_price = 5000

print("wellcome to resturant\n\n pizza ............ 250,000t\n burger ........... 180,000t\n sandwich ......... 120,000t\n coca ............. 5,000t\n")

sefarsh_pizza = int(input("lotfn tedade 'PIZZA' morede nazare khod ra vared namayid : "))
sefarsh_burger = int(input("lotfn tedade 'BURGER' morede nazare khod ra vared namayid : "))
sefarsh_sandwich = int(input("lotfn tedade 'SANDWICH' morede nazare khod ra vared namayid : "))
sefarsh_coca = int(input("lotfn tedade 'COCA' morede nazare khod ra vared namayid : "))


if sefarsh_pizza < 0 or sefarsh_burger < 0 or sefarsh_sandwich < 0 or sefarsh_coca < 0 :
    print("YOU ARE CRAZY")

else :

    price = (sefarsh_pizza * pizza_price)+(sefarsh_burger * burger_price)+(sefarsh_sandwich * sandwich_price)

    if price >= 500000 :

        print("\n\n\n factore shoma :\n")

        if sefarsh_pizza > 0 :

            print("pizaa      ",sefarsh_pizza," adad   ", sefarsh_pizza*pizza_price , " toman")
        if sefarsh_burger > 0 :

            print("burger     ",sefarsh_burger," adad   ", sefarsh_burger*burger_price , " toman")
        if sefarsh_sandwich > 0 :

            print("sandwich   ",sefarsh_sandwich," adad   ", sefarsh_sandwich*sandwich_price , " toman")
        if sefarsh_coca > 0 :

            print("coca       ",sefarsh_coca," adad   ", " free  " " toman")


        print("\nmablaghe sefareshe shoma ", price , "toman mibashad\n")

        if sefarsh_pizza + sefarsh_burger + sefarsh_sandwich >= 50 :
            print("in hame ghaza che khabare sheytoon ? adress bede manam miam\n")
        

    else :

        print("\n\n factore shoma :\n")

        if sefarsh_pizza > 0 :

            print("pizaa      ",sefarsh_pizza," adad   ", sefarsh_pizza*pizza_price , " toman")
        if sefarsh_burger > 0 :

            print("burger     ",sefarsh_burger," adad   ", sefarsh_burger*burger_price , " toman")
        if sefarsh_sandwich > 0 :

            print("sandwich   ",sefarsh_sandwich," adad   ", sefarsh_sandwich*sandwich_price , " toman")
        if sefarsh_coca > 0 :

            print("coca       ",sefarsh_coca," adad   ", sefarsh_coca*coca_price , " toman")

        price = price +(sefarsh_coca * coca_price)
        print("\n mablaghe sefareshe shoma ", price , "toman mibashad\n\n")