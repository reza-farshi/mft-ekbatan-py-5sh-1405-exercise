

# # ============================================================
# PROJECT: Advanced Number Range Analyzer
# تمرین تحلیل پیشرفته‌ی اعداد در یک بازه
# ============================================================
#
# هدف برنامه:
# گرفتن دو عدد مثبت از کاربر و تحلیل تمام عددهای بین آن‌ها.
#
# ورودی:
# - start : ابتدای بازه
# - end   : انتهای بازه
#
# قوانین ورودی:
# - start باید حداقل 1 باشد.
# - end باید بزرگ‌تر یا مساوی start باشد.
# - اگر بازه اشتباه بود، دوباره از کاربر ورودی گرفته شود.
# ------------------------------------------------------------
# گزارش نهایی برنامه باید شامل این موارد باشد:
# ------------------------------------------------------------
#
# - تعداد کل عددهای بازه
# - مجموع همه‌ی عددهای بازه
# - تعداد عددهای اول
# - تعداد پالیندروم‌ها
# - تعداد عددهای کامل
# - تعداد آرمسترانگ‌ها
# - تعداد هارشادها
#
# - مجموع همه‌ی عددهای اول
# - میانگین عددهای اول
# - کوچک‌ترین عدد اول
# - بزرگ‌ترین عدد اول
#
# - عددی که بیشترین تعداد مقسوم‌علیه را دارد
# - تعداد مقسوم‌علیه‌های آن عدد
#
# - عددی که بیشترین مجموع رقم را دارد
# - مقدار آن مجموع رقم
#
# - طولانی‌ترین زنجیره‌ی پالیندروم‌های پشت‌سرهم
#
# - بیشترین فاصله بین دو عدد اول پشت‌سرهم
# - نمایش دو عدد اولی که این فاصله بینشان بوده
#
# مثال:
# 2   -> Prime Palindrome Harshad
# 6   -> Perfect Harshad
# 11  -> Prime Palindrome Harshad
# 153 -> Armstrong Harshad
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
#
# ممنوع:
# list, tuple, set, dict
# str
# def
# sum, max, min, sort
#
# ============================================================


sum_numbers = 0
prime_num = 0
perfect_num = 0
harshad_num = 0
palindrome_num = 0
armestrong_num = 0
sum_prime = 0
prime = 0
min_prime = 0
max_prime = 0
f_prime = 0
max_div = 0
max_div_num = 0
max_sum_arqam = 0
max_sum_arqam_num = 0
tafazol_prime = 0
max_tafazol_prime = 0
min_prime_t = 0
max_prime_t = 0

while True :

    start_num = int(input("please enter the first number :"))

    end_num = int(input("please enter the last number :"))

    if start_num < 1 :
        print("first number incorrect")
        continue
    elif end_num < start_num or end_num < 1 :
        print("last number is incorrect")
        continue
    else :
        break


total_number = end_num - start_num + 1

for i in range(start_num,(end_num+1)) :
    sum_numbers = sum_numbers + i



number = start_num
while True :

    if number == end_num + 1 :
        break
    
    div = 0
    sum_div = 0
    


    for i in range((number-1),0,-1):

        if number % i == 0 :
            div +=1
            sum_div = sum_div + i
            
    
    if div == 1 :
        prime_num +=1
        sum_prime = sum_prime + number
        prime = number


    if prime_num == 1 :
        min_prime = number
        max_prime = number
        f_prime = number
    

        
    if prime < min_prime :

        min_prime = prime
    
    if prime > max_prime :

        max_prime = prime
        
    
    tafazol_prime = prime - f_prime



    if prime_num == 2 :
        max_tafazol_prime = tafazol_prime
    
    if tafazol_prime > max_tafazol_prime :
        max_tafazol_prime = tafazol_prime
        min_prime_t = f_prime
        max_prime_t = prime

    f_prime = prime

    if sum_div == number :
        perfect_num += 1
    
    if number == start_num :
        max_div = div


    if div > max_div :
        max_div = div
        max_div_num = number

    
    makoos = 0
    sum_arqam = 0
    raqam_num = 0



    number_1 = number

    while True :
        b = number_1 % 10
        number_1 = int(number_1 / 10)
        makoos = makoos * 10 + b
        sum_arqam = sum_arqam + b
        raqam_num += 1
        if number_1 < 1 :
            break


    if number == start_num :
        max_sum_arqam = sum_arqam


    if sum_arqam > max_sum_arqam :
        max_sum_arqam = sum_arqam
        max_sum_arqam_num = number
    
    if makoos == number :
        palindrome_num +=1
    
    if number % sum_arqam == 0 :
        harshad_num += 1
    
    number_arm = number
    armestrong = 0

    while True :

        b = number_arm % 10
        number_arm = int(number_arm / 10)
        armestrong = armestrong + b**raqam_num
        if number_arm < 1 :
            break
    
    if armestrong == number :
        armestrong_num += 1

    

    number += 1

print("total numbers :" , total_number)

print( "prime numbers :" , prime_num)

print("palindrome numbers :" , palindrome_num)

print("perfect numbers :", perfect_num)

print("armstrong numbers :" , armestrong_num)

print("harshad numbers :" , harshad_num)

print()

print("sum of all numbers :" , sum_numbers)

print("sum of prime numbers :" , sum_prime)

avrage_prime = sum_prime / prime_num

print("average of prime numbers :" , avrage_prime)

print()

print("smallest prime :" , min_prime)

print("largest prime : " , max_prime)

print("number with most divisors :" , max_div_num , "by" , max_div , "divisors")

print("largest digit sum :", max_sum_arqam , "for", max_sum_arqam_num)

print()

print("largest prime gap :" , max_tafazol_prime , " between " , min_prime_t , " and " , max_prime_t)

