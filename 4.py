#pishnehade lebas bar asase dama

print(("\n wellcome to my program\n"))

temp = float(input("pleas enter temp :"))

if temp <=0 :

    print("lebase zakhim bepooshid")

    rain = input(" aya baran mibarad ? yes or no\n")
    if rain == "yes" :
        print("hatman chatr be hamrah dashte bashid")
    else :
        print("rooze khoobi dashte bashid")

elif 0<temp<=10 :
    print("lebase garm bepooshid")

    rain = input(" aya baran mibarad ? yes or no\n")
    if rain == "yes"  :
        print("hatman chatr be hamrah dashte bashid")
    else :
        print("rooze khoobi dashte bashid")

elif 10<temp<=25 :
    print("hava motadel ast")

    rain = input(" aya baran mibarad ? yes or no\n")
    if rain == "yes" :
        print(rain)
        print("hatman chatr be hamrah dashte bashid")
    else :
        print("rooze khoobi dashte bashid")

elif 25<temp :
    print("lebase khonak bepooshid")