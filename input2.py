#this will ask for user input
import sys
import turtle
import random


class DrawObject():

      def __doc__(self):
            'Method for drawing Objects of any kind'

      def __init__(self):
            pass

      def Square(self, color_type, size):
            try:
                  import turtle
                  sam = turtle.Turtle()
                  for i in [0,1,2,3]:
                        sam.speed(5)
                        sam.forward(self.size)
                        sam.speed(2.5)
                        sam.right(90)
                        sam.speed(5)
                        sam.fillcolor(self.color_type)

            except Exception:
                  pass

      def Rectangle(self, color_type, x, y):
            try:
                  import turtle
                  sam = turtle.Turtle()
                  
                  sam.speed(5)
                  sam.forward(self.x)
                  sam.speed(2.5)
                  sam.right(90)
                  sam.speed(5)
                  sam.forward(self.y)
                  sam.right(90)
                  sam.forward(self.x)
                  sam.right(90)
                  sam.forward(self.y)
                  sam.fillcolor(self.color_type)

            except Exception:
                  pass
            



rand_reply = random.choice(seq=('My Boss', 'My Creator', 'My Partner'))

name= str(input("whats your name? "));
n = name
if (n == "sam"):
      for i in rand_reply:
            pass
      print(rand_reply)
elif (n == "mario"):
      print("Wait, i know you, you are my co-programmer")      
elif (n == "yusupha"):
      print("yeah, the big research guy")
elif (n == "clement"):
      print("Never forgets the motto's")
elif (n == "ruben"):
      print("The headmaster guy, boy i beg u plz be a headmaster")
elif (n == "desire"):
      print("ezeh lokin The education buaa, physics boy,maths boy, chemistry boy, and...")
elif (n == "omar"):
      print("sawaneh the always active boy, undifined")
elif (n == "ansumana"):
      print("Umpa mendy the prison headmaster")
elif (n == "amadou"):
      print("bobo the football analist")
elif (n == "lamin"):
      print("internet browser for football")
elif (n == "sarjo"):
      print("Girl with the laughing sickness")
elif (n == "ramatoulie"):
      print("My foolish little chicken")
elif (n == "baby ara"):
      print("hm that's my bosses better half, sam")
elif (n == "ara"):
      print("hi our wife, i miss you deh")
elif (n == "jola"):
      print("hi serious girl")
elif (n == "tida"):
      print("quite girl")
elif (n == "pa seedey"):
      print("technical drawer, 50% degree physist")
elif (n == "vincent"):
      print("hm the fake pastor, hardworking and very playful, ")
elif (n == "larion"):
      print("simply needs a high tech brain fixer")
elif (n == "mr.jawara"):
      print("Our senoir hacker,")
elif (n == "ismaila"):
      print("Yeah the real guy, heard working")
elif (n == "victor"):
      print("hardwording per perfect")
elif (n == "salieu"):
      print("Sheick gibba")
elif (n == "tijan"):
      print("ohh bobo, why not just make it amadou,you know you fulas. okay")
elif (n == ""):
      print("")
elif (n == ""):
      print("")
elif (n == ""):
      print("")
elif (n == ""):
      print("")
elif (n == ""):
      print("")      
elif (n == ""):
      print("")      
else:
      print ("nice to meet you " + name);




gender = input("Are you a male or female ")

try:
      grade= int(input("Which grade are you in " + name + "? "))
except ValueError:
      print('Enter only your Grade')

a=grade;
if(0<a & a<=12):
      print("Quite impressive,Keep up the pase!")
elif(a>12):
      print("Stop lying, is their anything like grade " + str(grade))
elif(a<1):
     print("Don't play with me y!!!")
else:
     print("I don't know woo!")
age= int(input("Whats your age " + name + "! " ))
y=age;
if(y>=25):
     print("You are a big boy to be in school, go home!")
elif((y>20) and (y<=24) and (a<11)):
     print("You big boy in grade " + str(grade))
elif((y<17) and (a>=11)):
     print("You small boy in grade " + str(grade))
else:
     print("grown up")

     
color= str(input("Whats your favourite color " + name + "! " ))
c = color;
if (c == "blue"):
      print(color + " is my favourite, boys color")
elif (c == "pink"):
      print(color + " is a girls color")
elif (c == "red"):
      print("That's my little chicken's color, no comments")
elif ((c == "pink") and (gender == "male")):
      print("A boy desiring girls color")
elif ((c == "blue") and (gender == "female")):
      print("A girl desiring boys color")
else:
      print(color + " is a nice color " + name)
girls= int(input("How many gilrs do you have "));
x=girls;
if (x<=2):
          print("that's good");
elif(2<x<10):
             print("you are hot, men!!!");
elif(11<x<25):
          print("why are you a big bandit");
else:
           print("Girls will impregnate you");

school= str(input("Which school are you in " + name ));
s=school;
if(s=="st. peters"):
      print("st. perters is the best, i was also there");
elif(s=="methodist"):
      print("The most boring school ever");
elif(s=="nusrat"):
      print("Examination school, office dogs");
elif(s=="gambia high"):
      print("oldest school in the gambia");
elif(s=="sos"):
      print("school of sqage");      
elif(s=="st. augustine"):
      print("boys arena, quiter");
elif(s=="st. thereses"):
      print("among the best");
else:
      print("Find a better one, ohhhhhh");

food = input("Are you hungry?(yes/no)(y/n) ");
f = food;
if ((f == "yes") or (f == "y")):
      print("Give me money let me buy bread for you, trust me!")
else:
      print("Well that's cool, what did you eat")
'''     eat = sys.stdin.readline()

if (eat == "bread and beans"):
      print("Ahh i don't like it that much")
elif (eat == ""):
      print("")
elif (eat == ""):
      print("")      
elif (eat == ""):
      print("")
elif (eat == ""):
      print("")      
elif (eat == ""):
      print("")
elif (eat == ""):
      print("")
elif (eat == ""):
      print("")
elif (eat == ""):
      print("")
elif (eat == ""):
      print("")
elif (eat == ""):
      print("")
elif (eat == ""):
      print("")
elif (eat == ""):
      print("")
elif (eat == ""):
      print("")
elif (eat == ""):
      print("")
elif (eat == ""):
      print("")
else:
      print("Never heard of it!")
'''

Temperature = input("What's the temperature outside(oC) ")
t = Temperature;
if ((x>=13) or (x<=20)):
      print("waw, that's preety cold, take a jacket(yes, ok or no)")
      reply = sys.stdin.readline()
      if ((reply == "yes") or (reply == "y")):
            print("Good good, it's always nice to command ")
      elif ((reply == "no") or (reply == "n")):
            print("what an impolite reply")
      else:
            print("ok no problem")
elif ((20<x) or (x<=37)):
      print("thats pretty chilly, hope you bought ice at the market to meet the condition(y/n)")
      reply2 = sys.stdin.readline()
      if ((reply2 == "y") or (reply2 == "yes")):
            print("yeah i knew it " + name)
      elif ((reply2  == "n") or (reply2 == "no")):
            print("ok stubbornie")
      else:
            print("ok big guy")
elif ((38<=x) or (x<=65)):
      print("Thats pretty hot boy, hope you took bath in the morning(yes/no)")
      reply3 = sys.stdin.readline()
      
      if ((reply3 == "yes") or (reply3 == "y")):
            print("That was what i expected")
      elif ((reply3 == "no") or (reply3 == "n")):
            print("OHH no leave me boy!, " + name)
      else:
            print("ok no problem1")
elif (x < 12):
      print("Don't try to fool me ok, the least i've seen in this country is 16 degrees")
elif (x > 65):
      print("Do you want to boil, don't pray that for us in the gambia ok")
else:
      print("ok what ever!")




money = input("Can you plz give me some money, am hungry ")
m = money


reply4 = input("Now you have completed, could you like me to draw a shape(yes or no)\n")
if (reply4 == "yes"):
      reply5 = input("Which shape do you want me to print for you /n 1.square 2.rectangle 3.hexagon 4.triangle 5.diangle 6.circle 7.elipse\n")
      if (reply5 == "1"):
            print("Let me draw a square for you")
            print("Drawing...")
            
            Draw = DrawObject()
            Draw.Square(c, 110)
      
      elif (reply5 == "2"):
            print("Let me draw a rectangle for you")
            print("Drawing...")

            Draw = DrawObject()
            Draw.Rectangle(c, 150, 100)

      elif (reply5 == "3"): 
            print("b")
      elif (reply5 == "4"):
            print("c")
      elif (reply5 == "5"):
            print("d")
      elif (reply5 == "6"):
            print("e")
      elif (reply5 == "7"):
            print("f")
      else:
            print("g")
else:
      print("Ok thanks for playing me till next time, Goodbye!!! " + name)
      print("By: sam@pragrammer")
      print("    @@   @@   @@    @@  @@@                             ")
      print("   @    @  @  @ @  @ @  @@@ @@@ @@@ @@@ @@@@ @@@ @@ @@ @@ @@ @@@@ @@@@                ")
      print("    @@ @ @@ @ @  @@  @  @   @   @@@ @@@ @@   @@@ @ @ @ @ @ @ @@@  @@    ")
      print("     @@      @@      @                @        @             @@@@   ")
      print("   @@ @      @@      @              @@@                     ")











      
     
        
