

#mohasebe ghabze barghe sade

print("\n wellcome to my program \n")

price_per_kw1_100 = 1000
price_per_kw100_200 = 1500
price_per_kw200_ = 2500

masraf_bargh = float(input("please enter your consumption :"))

if 0 < masraf_bargh <= 100 :
     
    price = masraf_bargh * price_per_kw1_100

    print("hazine barghe shoma", price ,"toman mibashad")

    
if 100 < masraf_bargh <=200 :

    price = (100 * price_per_kw1_100) + ((masraf_bargh - 100) * price_per_kw100_200)

    print("hazine barghe shoma", price ,"toman mibashad")

if 200 < masraf_bargh :

    price = (100*price_per_kw1_100) + (100*price_per_kw100_200) + ((masraf_bargh-200)*price_per_kw200_)

    print("hazine barghe shoma", price ,"toman mibashad")