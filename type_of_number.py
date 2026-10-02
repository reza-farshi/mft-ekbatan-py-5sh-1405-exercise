

# ============================================================
# PROJECT: Number Analyzer
# تمرین تحلیل یک عدد
# ============================================================
#
# هدف برنامه:
# گرفتن یک عدد مثبت از کاربر و بررسی ویژگی‌های مختلف آن.
#
# برنامه باید تا وقتی کاربر عدد 0 وارد نکرده، ادامه پیدا کند.
# اگر کاربر 0 وارد کرد، برنامه پیام خداحافظی چاپ کند و تمام شود.
#
# ------------------------------------------------------------
# برای هر عدد واردشده، برنامه باید این موارد را بررسی کند:
# ------------------------------------------------------------
#
# 1) Prime Number / عدد اول:
#    - بررسی شود که عدد اول هست یا نه.
#    - عدد اول فقط دو مقسوم‌علیه دارد: 1 و خودش.
#    - مثال:
#      17 --> Prime
#      12 --> Not Prime
#
# 2) Divisors Count / تعداد مقسوم‌علیه‌ها:
#    - تعداد مقسوم‌علیه‌های عدد حساب و چاپ شود.
#    - مثال:
#      12 --> 6 divisors
#
# 3) Divisors Sum / مجموع مقسوم‌علیه‌ها:
#    - مجموع تمام مقسوم‌علیه‌های عدد حساب شود.
#    - مثال:
#      divisors of 12: 1, 2, 3, 4, 6, 12
#      sum: 28
#
# 4) Perfect Number / عدد کامل:
#    - مجموع مقسوم‌علیه‌ها، به‌جز خود عدد، با خود عدد مقایسه شود.
#    - اگر برابر بودند، عدد کامل است.
#    - مثال:
#      6 = 1 + 2 + 3
#      پس 6 یک عدد کامل است.
#
# 5) Reverse Number / معکوس عدد:
#    - رقم‌های عدد بدون استفاده از str برعکس شوند.
#    - مثال:
#      12340 --> 4321
#
# 6) Palindrome / پالیندروم:
#    - اگر عدد و معکوس آن با هم برابر باشند، عدد پالیندروم است.
#    - مثال:
#      121 --> Palindrome
#      4554 --> Palindrome
#      123 --> Not Palindrome
#
# 7) Digit Count / تعداد رقم‌ها:
#    - تعداد رقم‌های عدد با while حساب شود.
#    - مثال:
#      153 --> 3 digits
#
# 8) Armstrong Number / عدد آرمسترانگ:
#    - هر رقم به توان تعداد رقم‌ها برسد.
#    - مجموع آن‌ها اگر برابر خود عدد بود، عدد آرمسترانگ است.
#    - مثال:
#      153 = 1^3 + 5^3 + 3^3
#      153 --> Armstrong Number
#
#
# ------------------------------------------------------------
# محدودیت‌های تمرین:
# ------------------------------------------------------------
#
# مجاز:
# input, int, print
# if, elif, else
# while, for
# break, continue
# +, -, *, /, //, %, **
#
# ممنوع:
# list, str, def
# sum, max, min, sort
#
# ============================================================




while True :

    num = int(input("please enter the number : "))

    if num == 0 :
        print("goodbye")
        break

    j = 0
    s = 0

    start = int(num/2)
    
    print("divisors is :" , end=" ")

    for i in range(start,0,-1):

        if num % i == 0 :
            s = s + i
            j += 1
            print(i , end=" ")
    print()

    if j == 1 :
        print(num , "is prime")
    else :
        print(num,"in not prime")

    print("divisors count :", j , " \n divisors sum :",s)

    if s == num :
        print(num , "is a perfect number")
    else :
        print(num , "is not perfect number")

    makoos = 0
    num1 = num
    while True:

        b = num1 % 10
        num1 = int( num1 / 10 )
        makoos = makoos*10 + b
        if num1 < 1 :
            break
    print( "reverse :" , makoos)    

    if makoos == num :
        print( num , " is palindrome number")
    else :
        print(num , " is not palindrome number")

    r = 0
    armestrang = 0
    num2 = num
    num3 = num

    while True :
        num2 = num2/10
        r += 1
        if num2 < 1 :
            break

    while True:

        b = num3 % 10
        num3 = int( num3 / 10 )
        armestrang = armestrang + b**r
        if num3 < 1 :
            break

    if armestrang == num :
        print(num , " is armestrong number")
    else :
        print(num , " is not armestrong number")

    print()
    print()
    
    
