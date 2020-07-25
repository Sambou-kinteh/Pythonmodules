
aim_main = '''          This has been developed by Sam kinteh
          For the purpose of making Calculations
                in Matrices(3x3f Easier
                    in the form
                ax + by + cz = Equivalent
                dx + ey + fz = Equivalent
                gx + hy + iz = Equivalent
                    Constants(X,Y,Z)
                '''

print(aim_main)

while(True):
    try:
        #valS for calc
        print('For Equation 1:')
        A = int(input('A: '))
        B = int(input('B: '))
        C = int(input('C: '))
        print('For Equation 2:')
        D = int(input('D: '))
        E = int(input('E: '))
        F = int(input('F: '))
        print('For Equation 3:')
        G = int(input('G: '))
        H = int(input('H: '))
        I = int(input('I: '))

        #Equivalent
        print('Equivalents For All Three Equations')
        AEquals=eq1 = int(input('Value For Equation1: '))
        BEquals=eq2 = int(input('Value For Equation2: '))
        CEquals=eq3 = int(input('Value For Equation3: '))
        #constants
        print('Constants For All Three Equations')

        AConstant= str(input('First Constant: '))
        BConstant= str(input('Second Constant: '))
        CConstant = str(input('Third Constant: '))
        break

    except ValueError:
        print('Incorrect Entry, Try Again!\n')


class Matrice:
    while(True):
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
 
        x_value = DetOfAxMat/DetOfTrueMat
        y_value = DetOfAyMat/DetOfTrueMat
        z_value = DetOfAzMat/DetOfTrueMat
        
        #print('\n')
        print('\nValues:\n')
        print('{0} = {1} or {2}/{3}'.format(AConstant, x_value, DetOfAxMat, DetOfTrueMat))
        print('{0} = {1} or {2}/{3}'.format(BConstant, y_value, DetOfAyMat, DetOfTrueMat))
        print('{0} = {1} or {2}/{3}'.format(CConstant, z_value, DetOfAzMat, DetOfTrueMat))
        break

        
#------------------Another way of doing it, just to change the function name in the if block to main() from Matrice()-------------------#
'''def main():
    
    print('{0}: {1} or {2}/{3}'.format(AConstant, x_value, DetOfAxMat, DetOfTrueMat))
    print('{0}: {1} or {2}/{3}'.format(BConstant, y_value, DetOfAyMat, DetOfTrueMat))
    print('{0}: {1} or {2}/{3}'.format(CConstant, z_value, DetOfAzMat, DetOfTrueMat))'''


if __name__ == '__main__':
    Matrice()






















    

