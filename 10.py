#dastgahe khodpardaze sade


print("\n wellcome to my program\n")

main_password = "4321"

user_password = input("lotfan passworde khod ra vared namayid :")

if user_password == main_password :

    mojodi = int(input("\n lotfan mojodie khod ra vared namayid :"))

    bardasht = int(input("\n lotfan mablaghe bardasht ra vared namayid :"))

    if 0 < bardasht < mojodi :

        if bardasht % 50000 == 0 :
            
            baghi_mande = mojodi - bardasht

            print("mablaghe",bardasht,"toman az hesabe shoma ba movafaghiat bardasht shod \n baghi mande hesabe shoma",baghi_mande,"toman mibashad \n")
        else :
            print("mizane bardasht bayad mazrabi az 50,000 toman bashad")
    elif bardasht <= 0 :
        print("mablaghe morede nazar baraye bardasht sahih nist")
    else :
        print("mojodi nakafi")
else :
    print("password incorrect")