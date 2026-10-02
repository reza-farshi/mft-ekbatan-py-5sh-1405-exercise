#mohasebe shakhese toode badani bmi


print("\n wellcome to my7 program\n")

weight = 0
height = 0

weight = float(input("please enter weight :"))

height = float(input("please enter height :"))

if height > 100 :
    height = height/100

bmi = weight / (height**2)

if 0 < bmi < 18.5 :
    print("bmi :" ,round(bmi) ,"kamboode vazn","vazne monase ghade shoma",round( 18.5*(height**2)), "ela" ,round( 25*(height**2)),"kg mibashad")
elif 18.5 < bmi <25 :
    print("bmi :" , round(bmi) ,"vazne monaseb")
elif 25 < bmi <30 :
    print("bmi :" , round(bmi) ,"ezafe vazn","vazne monase ghade shoma",round( 18.5*(height**2)), "ela" ,round( 25*(height**2)),"kg mibashad")
elif bmi > 30 :
    print("bmi :" , round(bmi) ,"chaghi","vazne monase ghade shoma",round( 18.5*(height**2)), "ela" ,round( 25*(height**2)),"kg mibashad")
else :
    print("YOU ARE DEAD")