#baresi mojodi hesabe banki

print("\n wellcom to my program \n")

mojodi = 0
mablagh_bardasht = 0
mojodi_jadid = 0

mojodi = int(input("lotfan mojodi hesabe khod ra vared konid : \n"))

if mojodi == 0 :
    print("mojoodi nemitavanad sefr bashad\n")
else :

    mablagh_bardasht = int(input("lotfan mablagh morede nazar barye bardash ra vared namayid :\n"))

    if mablagh_bardasht == 0 :
        print("mablaghe bardasht nemitavanad sefr bashad\n")
    else :
        if mablagh_bardasht > mojodi :
            print("mablaghe bardasht nemitavanad bishtar az mojodi bashad\n")
        else :
            
            mojodi_jadid = mojodi - mablagh_bardasht
            if mojodi_jadid <= 100000 :
                print("mablaghe" , mablagh_bardasht , "toman ba movafaqiat az hesabe shoma bardasht shod\n")
                print("baghi mande hesabe shoma :",mojodi_jadid,"toman mibashad\n")
                print("***hoshadr*** mojodi hesabe shoma kamtar az 100.000 toman ast***hoshadr***\n")
            else :
                print("mablaghe" , mablagh_bardasht , "toman ba movafaqiat az hesabe shoma bardasht shod\n")
                print("baghi mande hesabe shoma :",mojodi_jadid,"toman mibashad\n")