#entekhabe noe ersale sefaresh


print("\n wellcome to my program \n")

ersal_normal = 50000

ersal_fast = 100000

mablagh_kharid = int(input("lotfan mablaghe kharid ra vared konid\n"))

ersal_type = input("lotfan modele ersale khod ra moshakhas namayid : \n normal or fast \n")

if ersal_type == "normal" :
    if mablagh_kharid >= 2000000 :
        print("ersale shoma rayegan mibashad\n")
    else :
        print("hazine ersale shoma",ersal_normal," toman mibashad\n")
if ersal_type == "fast" :
    print("hazine ersale shoma",ersal_fast," toman mibashad\n")
else :
    print("modele ersale entekhabie shoma mojod nemibashad")