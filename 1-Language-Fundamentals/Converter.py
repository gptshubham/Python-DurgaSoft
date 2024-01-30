# dictionary containing number values
d1 = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
         11:'Eleven',12:'twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',
      19:'Nineteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
d10 = {2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}
# function to convert numbers into words
def conversion(n):
    if type(n) == int:
        word = ''
        if n in d1:
            word = d1[n]
        elif 20 < n < 100:
            unit = n%10
            tenth = n-unit
            word = d1[tenth]+' '+d1[unit]
        elif 99 < n <= 999:
            unit = n%10
            n //= 10
            tenth = n % 10
            n //= 10
            if unit == 0:
                if tenth == 0:
                    word = d1[n] + ' Hundred'
                elif tenth == 1:
                    word = d1[n] + ' Hundred and ' + d1[(tenth * 10) + unit]
                else:
                    word = d1[n] + ' Hundred and ' + d10[tenth]
            elif tenth == 0:
                word = d1[n] + ' Hundred and ' + d1[unit]
            elif tenth == 1:
                word = d1[n] + ' Hundred and ' + d1[(tenth * 10) + unit]
            else:
                word = d1[n] + ' Hundred and ' + d10[tenth] + ' ' + d1[unit]
        return word
    else:
        return 'Invalid Input!'

# # testing conversion()
# # taking input from user
# n = int(input('Enter a Number : '))
# # calling conversion() and storing the value in result variable
# result = conversion(n)
# # printing result to console
# print(result)
