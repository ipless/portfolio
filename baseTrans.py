def base_num(num, base):
    new_num = ''
    while num > 0:
        new_num = str(num % base) + new_num
        num //= base
    return new_num

import pandas as pd
import xlsxwriter as exl

name=input('имя файла: ')

workbook   = exl.Workbook(name+'.xlsx')
worksheet1 = workbook.add_worksheet()

base=int(input("основание: "))
to_since=int(input("до порядка: "))
for a in range(base**to_since):
    answ=[]
    for b in range(base**to_since):
        worksheet1.write(a, b, base_num(a*b,base))
print('done')
workbook.close()
