#we first import sys
import sys
print("Hi User")
print("\t\t    What do you want me to convert for you")
print("\tChoose from the alternative list below(from example to example)")
print(">>Centimeter")
print(">>Millimeter")
print(">>Kilometer")
print(">>Meter\n")

fro = input("FROM:\n")
to = input("TO:\n")
#moving to the centimeter block
if ((fro == "centimeter") and (to == "millimeter")):
    print("Plz Input Your value in centimeters")
    print("Centimeter: ")
    cent1 = sys.stdin.readline()
    cent_mill = (float(cent1)*10)
    print("Millimeter = ",cent_mill,"mm")
    print("Have a good day")
elif ((fro == "centimeter") and (to == "kilometer")):
    print("Plz Input Your value in centimeters")
    print("Centimeters: ")
    cent2 = sys.stdin.readline()
    cent_kilo = (float(cent2)/100000)
    print("Kilometer = ",cent_kilo,"km")
    print("Have a nice day")
elif ((fro == "centimeter") and (to == "meter")):
    print("Plz Input Your value in centimeters")
    print("Centimeter: ")
    cent3 = sys.stdin.readline()
    cent_mete = (float(cent3)/100)
    print("Meter = ",cent_mete,"m")
    print("Have a nice day")
#moving to the millimeter block
elif ((fro == "millimeter") and (to == "centimeter")):
    print("Plz Input Your value in millimeters")
    print("Millimeter: ")
    mill1 = sys.stdin.readline()
    mill_cent = (float(mill1)/10)
    print("Centimeter = ",mill_cent,"cm")
    print("Have a nice day")
elif ((fro == "millimeter") and (to == "kilometer")):
    print("Plz Input Your value in millimeters")
    print("Millimeter: ")
    mill2 = sys.stdin.readline()
    mill_kilo = (float(mill2)/1000000)
    print("Kilometer = ",mill_kilo,"km")
    print("Have a nice day")
elif ((fro == "millimeter") and (to == "meter")):
    print("Plz Input Your value in millimeters")
    print("Millimeter: ")
    mill3 = sys.stdin.readline()
    mill_mete = (float(mill3)/1000)
    print("Meter = ",mill_mete,"m")
    print("Have a nice day")
#moving to the kilometer block
elif ((fro == "kilometer") and (to == "centimeter")):    
     print("Plz Input Your value in kilometers")
     print("Kilometer: ")
     kilo1 = sys.stdin.readline()
     kilo_cent = (float(kilo1)*100000)
     print("Centimeter = ",kilo_cent,"cm")
     print("Have a nice day")
elif ((fro == "kilometer") and (to == "millimeter")):
    print("Plz Input Your value in killometers")
    print("Kilometer: ")
    kilo2 = sys.stdin.readline()
    kilo_mill = (float(kilo2)*1000000)
    print("Miliimeter = ",kilo_mill,"mm")
    print("Have a nice day")
elif ((fro == "kilometer") and (to == "meter")):
    print("Plz Input Your value in kilometers")
    print("Kilometer: ")
    kilo3 = sys.stdin.readline()
    kilo_mete = (float(kilo3)*1000)
    print("Meter = ",kilo_mete,"m")
    print("Have a nice day")
#moving to the meter block
elif ((fro == "meter") and (to == "centimeter")):
    print("Plz Input Your value in meters")
    print("Meter: ")
    mete1 = sys.stdin.readline()
    mete_cent = (float(mete1)*100)
    print("Centimeter = ",mete_cent,"cm")
    print("Have a nice day")
elif ((fro == "meter") and (to == "millimeter")):    
    print("Plz Input Your value in meters")
    print("Meter: ")
    mete2 = sys.stdin.readline()
    mete_mill = (float(mete2)*100)
    mete_mill1 = (float(mete_mill)*10)
    print("Millimeter = ",mete_mill1,"mm")
    print("Have a nice day")

elif ((fro == "meter") and (to == "kilometer")):
    print("Plz Input Your value in meter")
    print("Meter: ")
    mete3 = sys.stdin.readline()
    mete_kilo = (float(mete3)/1000)
    print("Kilometer = ",mete_kilo,"km")
else:
    print("Goodbye!")
    
    
    
