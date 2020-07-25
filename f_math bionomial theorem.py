import math
print("\t\t\tInput In Here Your Values\n\n")
print("BIONOMIAL THEOREM\n")
a = int(input(">>a: "))
# x is constant
n = float(input(">>n: "))
x = float(input("coefficent of x: "))
bio1 = int(int(a)**int(n))
bio2 = int(x*(int(n)*(int(a)**(int(n)-1))))
bio3 = int(x*(int(n*(int(n)-1)/(math.factorial(2)))*int(a)**(int(n)-2)))
bio4 = int(x*(int(n*(int(n)-1)*(int(n)-2)/(math.factorial(3)))*int(a)**(int(n)-3)))





print("Bionomail = ",bio1 ,'+', str(bio2) + 'x +',  str(bio3) + 'x\u00b2 +',  str(bio4) + 'x\u00b3...')



#---------F_MAth parts will be having the same menu bar--------#
