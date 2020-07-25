#creating variables temp, kelvin, celsius and fareiheight
import sys
print("Hi User!, My name is sam and whats your name")
n = sys.stdin.readline()
print("You have a nice name, lets bigin ", n)
print("what do you want me to convert for you ")
cel = print("1. celsius to fareiheight")
faht = print("2. fareiheight to celsius")
cel2 = print("3. celsius to kelvin")
kel = print("4. kelvin to celsius")
kel2= print("5. fareiheight to kelvin, no direct conversion")
kel3= print("6. kelvin to fareiheight, no direct conversion")
reply = input("Choose a number:  ")
if (reply == "1"):
    print ("pass the value")
    print ("Temp in celsius: ")
    reply1 = sys.stdin.readline()
    Temp1 = (float(reply1) * float(1.8))+32
    print ("Temperature in Fareiheight for ",reply1,"celsius = ", Temp1,"*F")
    print("Have a good day", n)
elif (reply == "2"):
    print("pass the value")
    print("Temp in fareiheight: ")
    reply2 = sys.stdin.readline()
    Temp2 = (float(reply2)-32) / 1.8
    print ("Temperature in Celsius for ",reply2,"fareiheights = ", Temp2,"*C")
    print("Have a good day", n)
elif (reply == "3"):
    print("pass the value")
    print("Temp in celsius: ")
    reply3 = sys.stdin.readline()
    Temp3 = (273 + float(reply3))
    print ("Temperature in Kelvin for ",reply3,"celsius = ", Temp3,"*K")
    print("Have a good day", n)
elif (reply == "4"):
    print("pass the value")
    print("Temp in kelvin: ")
    reply4 = sys.stdin.readline()
    Temp4 = (float(reply4)-273)
    print ("Temperature in Celsius for ",reply4,"kelvins = ", Temp4,"*C")    
    print("Have a good day", n)
elif (reply == "5"):
    print("pass the value")
    print("Temp in fareiheight: ")
    reply5 = sys.stdin.readline()
    Temp5 = ((float(reply5)-32) / 1.8) + 273
    print ("Temperature in kelvin for ",reply5,"fareiheights = ", Temp5,"*K")
    print("Have a good day", n)
elif (reply == "6"):
    print("pass the value")
    print("Temp in kelvin: ")
    reply6 = sys.stdin.readline()
    c = (float(reply6)-273)
    Temp6 = (float(c) * float(1.8))+32
    print ("Temperature in fareiheight for ",reply6,"kelvins = ", Temp6,"*F")
    print("Have a good day", n)

