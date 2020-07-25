#calculating miles per gallon

print("This program claculates mpg")

#ask input from user

miles_driven = input("Enter miles driven: ")

#convert text entered to a float point number

miles_driven = float (miles_driven)

#get gallons used from the user

gallons_used = input("Enter gallons used: ")

#convert text entered to float piont number

gallons_used = float (gallons_used)

#calculate and print the answer

mpg = miles_driven / gallons_used
print ("Miles per gallon: ", mpg)
