import re
import matplotlib.pyplot as plt
import numpy as np

#mY Globals



def format1():
      try:
            global format1_num1
            global format1_num2
            #requirements for x2 + c
            format1_num1 = int(input('Enter the coefficent of x: '))
            format1_num2 = int(input('Enter the \'c\': '))
            print('y = %dx + %d\n' %(format1_num1, format1_num2))
            x_values = []
            y_values = []
            x_values.append(num1_range)
            for i in range(num1_range, num2_range):
                  if (num1_range <= i <= num2_range):
                        i += float(range_range)
                        x_values.append(i)
            for i in x_values:
                  y = (format1_num1 * i) + format1_num2
                  y_values.append(y)
            jointx = ''.join(str(x_values))
            jointy = ''.join(str(y_values))
            print('X Values :  ', jointx, end='')
            print('\nY Values:   ', jointy, end='')
            plt.plot(x_values, y_values, color = 'teal')
            plt.xlabel('X-Axis')
            plt.ylabel('Y-Axis')
            plt.show()
                        
            
      except Exception as msg:
            print('Only numbers allowed Please\n', msg)
            format1()

def format2():
      try:
            global format2_num1
            global format2_num2
            global format2_num3
            #requirements for x2 + x + c
            format2_num1 = int(input('Enter the coefficent of x\u00b2: '))
            format2_num2 = int(input('Enter the coefficent of X: '))
            format2_num3 = int(input('Enter the \'c\': '))
            print('y = %dx\u00b2 + %dx + %d\n' %(format2_num1, format2_num2, format2_num3))
            x_values = []
            y_values = []
            x_values.append(num1_range)
            for i in range(num1_range, num2_range):
                  if (num1_range <= i <= num2_range):
                        i += float(range_range)
                        x_values.append(i)
            for i in x_values:
                  y = (format2_num1 * ((i)**2))+ (format2_num2 * i) + format2_num3
                  y_values.append(y)
            jointx = ''.join(str(x_values))
            jointy = ''.join(str(y_values))
            print('X Values :  ', jointx, end='')
            print('\nY Values:   ', jointy, end='')
            plt.plot(x_values, y_values, color = 'teal')
            plt.xlabel('X-Axis')
            plt.ylabel('Y-Axis')
            plt.show()
            
      except Exception as msg:
            print('Only numbers allowed Please\n', msg)
            format2()

def format3():
      try:
            global format3_num1
            global format3_num2
            #requirements for x2 + c
            format3_num1 = int(input('Enter the coefficent of x\u00b2: '))
            format3_num2 = int(input('Enter the \'c\': '))
            print('y = %dx\u00b2 + %d\n' %(format3_num1, format3_num2))
            x_values = []
            y_values = []
            x_values.append(num1_range)
            for i in range(num1_range, num2_range):
                  if (num1_range <= i <= num2_range):
                        i += float(range_range)
                        x_values.append(i)
            for i in x_values:
                  y = (format3_num1 * ((i)**2)) + format3_num2
                  y_values.append(y)
            jointx = ''.join(str(x_values))
            jointy = ''.join(str(y_values))
            print('X Values :  ', jointx, end='')
            print('\nY Values:   ', jointy, end='')
            plt.plot(x_values, y_values, color = 'teal')
            plt.xlabel('X-Axis')
            plt.ylabel('Y-Axis')
            plt.show()
            
      except Exception as msg:
            print('Only numbers allowed Please\n', msg)
            format3()


print('Please divide the range of x into 4 parts, the no. and signs, thank you\n')

#input for the range

def requirements():
      try:
            global range_range
            global num1_range
            global num2_range
            global sign1_range
            global sign2_range
            
            print('Requirements; One')
            num1_range = int(input('\nEnter the starting range of f(x): '))
            sign1_range = input('Enter the first sign for starting i.e(< or <=): ')
            sign2_range = input('Enter the second sign for stoping i.e(< or <=): ')
            num2_range = int(input('Enter the stoping point of f(x): '))
            range_range = (input('Enter the intervals for the table: '))
            print('Evaluation : {0} {1} x {2} {3}  at {4} step intervals'.format(num1_range, sign1_range, sign2_range,num2_range, range_range))
            print('\nRequirements; Final')
            
      except Exception:
            print('Please, input types can ony be:- numbers or signs')
            requirements()

requirements()

print('If the evaluation meet your satisfaction, please kindly, (C)ontinue or (R)etype if not' )
response = input('> ')
if response.lower() == 'c':
      pass
else:
      
      while response.lower() != 'c':
            requirements()
            response = input('If the evaluation meet your satisfaction, please kindly, (C)ontinue or (R)etype if not\n' )

#list of formats
print('\nPlease choose the format of the function\n1. y = x\u00b2 + x + c\t2. y = x\u00b2 + c\t3. y = x + c')
response = input('> ')
if response == '1':
      format2()
elif response == '2':
      format3()
elif response == '3':
      format1()
else:
      print('Please enter a format for the equation')
           
'''
def f(x):
      y = 
'''

#####Just create a class boyyyyy
      
