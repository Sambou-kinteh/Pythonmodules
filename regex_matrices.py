import re


aim_main = '''          This has been developed by Sam kinteh
          For the purpose of making Calculations
                in Matrices(3x3) Easier
                    in the form
                ax + by + cz = Equivalent
                dx + ey + fz = Equivalent
                gx + hy + iz = Equivalent
                    Constants(X,Y,Z)\n\n'''

print(aim_main)
print('If you wish to exit, type exit at the biggening below or else press ENTER to begin\n')           

class Matrice:
    while(True):

        #INPUTS
        exit = input('')
        eqA = input('Equation 1: ')
        eqB = input('Equation 2: ')
        eqC = input('Equation 3: ')

        #PATTERNS TO MATCH
        pattern1 = r'(?P<num1_1>\d*)(?P<letter1_1>\w).\+.(?P<num1_2>\d*)(?P<letter1_2>\w).\+.(?P<num1_3>\d*)(?P<letter1_3>\w).\=.(?P<num1_4>\d*)'
        pattern2 = r'(?P<num2_1>\d*)(?P<letter2_1>\w).\+.(?P<num2_2>\d*)(?P<letter2_2>\w).\+.(?P<num2_3>\d*)(?P<letter2_3>\w).\=.(?P<num2_4>\d*)'
        pattern3 = r'(?P<num3_1>\d*)(?P<letter3_1>\w).\+.(?P<num3_2>\d*)(?P<letter3_2>\w).\+.(?P<num3_3>\d*)(?P<letter3_3>\w).\=.(?P<num3_4>\d*)'

        #SEARCHES
        search1 = re.search(pattern1, eqA, re.S)
        search2 = re.search(pattern2, eqB, re.S)
        search3 = re.search(pattern3, eqC, re.S)

        #VARIABLES
        #<------For Eq1------>
        var1_1 = search1.group('letter1_1')
        var1_2 = search1.group('letter1_2')
        var1_3 = search1.group('letter1_3')

        #<------For Eq2------>
        var2_1 = search2.group('letter2_1')
        var2_2 = search2.group('letter2_2')
        var2_3 = search2.group('letter2_3')

        #<------For Eq3------>
        var3_1 = search3.group('letter3_1')
        var3_2 = search3.group('letter3_2')
        var3_3 = search3.group('letter3_3')

        if ((exit == 'exit')):
            print('\nExiting From Matrices Advanced...')
            print('Thank You')
            break

        else:    

            if (var1_1 == var2_1) and (var1_1 == var3_1) and (var2_1 == var3_1):
                
                if (var1_2 == var2_2) and (var1_2 == var3_2) and (var2_2 == var3_2):
                    
                    if (var1_3 == var2_3) and (var1_3 == var3_3) and (var2_3 == var3_3):
                        
                        if search1:
                            #print('a= %s, b= %s, c= %s' % (search1.group('num1_1'), search1.group('num1_2'), search1.group('num1_3')))
                            A = int(search1.group('num1_1'))
                            B = int(search1.group('num1_2'))
                            C = int(search1.group('num1_3'))
                            AEquals = eq1 = int(search1.group('num1_4'))

                        if search2:
                            #print('x= %s, y= %s, z= %s' % (search2.group('num2_1'), search2.group('num2_2'), search2.group('num2_3')))
                            D = int(search2.group('num2_1'))
                            E = int(search2.group('num2_2'))
                            F = int(search2.group('num2_3'))
                            BEquals = eq2 = int(search2.group('num2_4'))

                        if search3:
                            #print('p= %s, q= %s, r= %s' % (search3.group('num3_1'), search3.group('num3_2'), search3.group('num3_3')))
                            G = int(search3.group('num3_1'))
                            H = int(search3.group('num3_2'))
                            I = int(search3.group('num3_3'))
                            CEquals = eq3 = int(search3.group('num3_4'))


                        else:
                            print('\nInvalid Syntax!')
                            print('Exiting...')
                            break

#<---------------------------Conditional block for the last variables------------------------------------>
                    else:
                        print('\nYour last variables are not the same, i.e(%s,%s and %s)' % (var1_3, var2_3, var3_3))
                        if var1_3 == var2_3:
                            firstvar = var1_3 = var2_3
                            firstvar *= 3
                            print('Recommend Using (%s) and try again\n' % (firstvar))
                            print('Exiting...')
                            break    

                        elif var1_3 == var3_3:
                            secondvar = var1_3 = var3_3
                            secondvar *= 3
                            print('Recommend Using (%s) and try again\n' % (secondvar))
                            print('Exiting...')
                            break

                        elif var2_3 == var3_3:
                            thirdvar = var2_3 = var3_3
                            thirdvar *= 3
                            print('Recommend Using (%s) and try again\n' % (thirdvar))
                        print('Exiting...')
                        break
#<---------------------------Conditional block for the middle variables------------------------------------>
                else:
                    print('\nYour second variables are not the same, i.e(%s,%s and %s)' % (var1_2, var2_2, var3_2))
                    if var1_2 == var2_2:
                        firstvar = var1_2 = var2_2
                        firstvar *= 3
                        print('Recommend Using (%s) and try again\n' % (firstvar))
                        print('Exiting...')
                        break    

                    elif var1_2 == var3_2:
                        secondvar = var1_2 = var3_2
                        secondvar *= 3
                        print('Recommend Using (%s) and try again\n' % (secondvar))
                        print('Exiting...')
                        break

                    elif var2_2 == var3_2:
                        thirdvar = var2_2 = var3_2
                        thirdvar *= 3
                        print('Recommend Using (%s) and try again\n' % (thirdvar))
                    print('Exiting...')
                    break                
#<-------------------------------------End of the middle block------------------------------------------->

#<------------------------------------Conditional block for the first blocked variables----------------------------------->
            else:
                print('\nYour first variables are not the same, i.e(%s,%s and %s)' % (var1_1, var2_1, var3_1))
                if var1_1 == var2_1:
                    firstvar = var1_1 = var2_1
                    firstvar *= 3
                    print('Recommend Using (%s) and try again\n' % (firstvar))
                    print('Exiting...')
                    break    

                elif var1_1 == var3_1:
                    secondvar = var1_1 = var3_1
                    secondvar *= 3
                    print('Recommend Using (%s) and try again\n' % (secondvar))
                    print('Exiting...')
                    break

                elif var2_1 == var3_1:
                    thirdvar = var2_1 = var3_1
                    thirdvar *= 3
                    print('Recommend Using (%s) and try again\n' % (thirdvar))
                print('Exiting')
                break
#<------------------------------------End of the third block----------------------------------->
            
            #Get our True Matrice First
            a1 = int(E*I)-(H*F)
            b1 = int(D*I)-(G*F)
            c1 = int(D*H)-(G*E)
            a2 = int(A*a1)
            b2 = int(B*b1)
            c2 = int(C*c1)
            DetOfTrueMat = a2 - b2 + c2

            #Find our Ax

            a3 = int(E*I)-(H*F)
            b3 = int(eq2*I)-(eq3*F)
            c3 = int(eq2*H)-(eq3*E)
            a4 = int(eq1*a3)
            b4 = int(B*b3)
            c4 = int(C*c3)
            DetOfAxMat = a4 - b4 + c4

            #Find our Ay

            a5 = int(eq2*I)-(eq3*F)
            b5 = int(D*I)-(G*F)
            c5 = int(D*eq3)-(eq2*G)
            a6 = int(A*a5)
            b6 = int(eq1*b5)
            c6 = int(C*c5)
            DetOfAyMat = a6 - b6 + c6

            #Find our Az

            a7 = int(E*eq3)-(H*eq2)
            b7 = int(D*eq3)-(eq2*G)
            c7 = int(D*H)-(G*E)
            a8 = int(A*a7)
            b8 = int(B*b7)
            c8 = int(eq1*c7)
            DetOfAzMat = a8 - b8 + c8
     
            x_value = round(DetOfAxMat/DetOfTrueMat, 3)
            y_value = round(DetOfAyMat/DetOfTrueMat, 3)
            z_value = round(DetOfAzMat/DetOfTrueMat, 3)
            
            #print('\n')
            print('\nValues:\n')
            print('{0} = {1} or {2}/{3}'.format(var1_1, x_value, DetOfAxMat, DetOfTrueMat))
            print('{0} = {1} or {2}/{3}'.format(var2_2, y_value, DetOfAyMat, DetOfTrueMat))
            print('{0} = {1} or {2}/{3}\n\n'.format(var3_3, z_value, DetOfAzMat, DetOfTrueMat))
            

if __name__ == '__main__':
    Matrice()
    
#class MSolver
#nested if statements for higher requiments(letters or variables or constants of the two eq)
#replacing the plus constant sign with an anytype input(operation)
    
