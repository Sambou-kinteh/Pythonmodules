#----------------------------------------Solving Logical Questions---------------------------------------#
import re

print("\t\t\tThis Interface Solves logical Questions\n\t\t\tIf you wish to Exit, Just Type 'Quit'")

class Solver():

    def __init__(self,num_one, num_two):
        self.num_one = num_one
        self.num_two = num_two
        
    while(True):
        
        ques_logic = input("Enter Your Question In Full:\n\n")

        if (ques_logic == "Quit"):
            print("You Just Exit from Sam.App")
            print("Have a nice day")
            break

        else:
            #patterns to be matched
            pattern_1 = r'(\w+)(?P<num_one>\W+)([-]|([a][n][d]))(?P<num_two>\W+)(\w+)?'
            pattern_2 = r'(.+)(?P<num_one_2>\W+)(.+)(?P<num_two_2>\W+)(.+)?'
                
            #additional stuff searches in other not to raise errors or exceptions
            search = re.search(pattern_1, ques_logic)
            other_form = re.search(pattern_2, ques_logic)

            if search:
                num_1 = int(search.group('num_one'))
                num_2 = int(search.group('num_two'))

        
                for i in range(num_1,num_2):
                    i += 1
                    if (i % 7) == 0:
                        print(i)



            elif other_form:
                num_3 = int(other_form.group('num_one_2'))
                num_4 = int(other_form.group('num_two_2'))

                for i in range(num_3,num_4):
                    i += 1
                    if (i % 7) == 0:
                        print(i)

            else:
                print("Incorrect Format!!!")
                print("Good Day")
 


def main(Solver):

    Solver()
                
                
            
        
