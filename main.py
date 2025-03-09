def int_to_roman(num):
    if  1<= num <=3999:
        symbols=['M', 'D', 'C', 'L', 'X', 'V', 'I']
        values= [1000, 500, 100, 50, 10,5, 1]
        roman= ''
        for i in range(len(values)):
            while num >= values[i]:
                roman +=symbols[i]
                num -= symbols[i]
        return roman 
    else:
        print('value must between 1 and 3999')
