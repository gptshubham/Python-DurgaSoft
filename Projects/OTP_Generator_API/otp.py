# OTP Generation Mini Project
# generate a 6 digit random number which can used as OTP
def otp():
    from random import randint
    # creating an Empty list 'otp'
    otp = []
    # generating OTP using for loop and randint()
    for i in range(6):
        otp.append(randint(0,9))
    # confirming otp list
    # print(otp)
    # converting int values of otp list into string using map()
    otp = list(map(str,otp))
    # print(otp)
    # joining otp
    otp = ''.join(otp)
    # printing output
    return otp

    # # Alternatively : Shortcut Method 😎 All Hail Time and Space Complexity
    # print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

    # # Alternatively : Ultra Shortcut -> Not Preferred as it can't generate otps starting from 0 like 000000,000001 etc.
    # print(randint(100000,999999))

# print(otp())