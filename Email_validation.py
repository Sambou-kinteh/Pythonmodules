import re
'''
pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print('it matched 1')
if re.match(pattern, "gray"):
    print('it matched 2')
if re.match(pattern, "grdy"):
    print('if matched 3')
'''
print("\t\t\tMail Recognition System\n")
print("\tType Quit/Exit or quit/exit to close the system\n\n")
while(True):
    mail = input("What is your Email address of any Type\n")

    if ((mail == "Quit") or (mail == "quit") or (mail == "Exit") or (mail == "exit")):
        print("Thank you for using my Sam_Validation system...")
        break
    else:
        try:
            pattern = r"(.+)@[e][m][a][i][l](.+)"
            pattern_1 = r"(.+)@[g][m][a][i][l](.+)"
            pattern_2 = r"(^(?P<upper>([A-Za-z]+)))(?P<nums>([0-9]+))@(?P<file>.)?[m][a][i][l](.)[c][o][m]$"
            pattern_3 = r"^(^(?P<words>([A-Za-z]+)))(?P<numbers>([0-9]+))@(?P<type>.)?([m][a][i][l](.)[c][o][m])$"
            search = re.search(pattern_2, mail)
            find = re.search(pattern_3, mail)

            if re.match(pattern, mail):
                if find:
                    print("Valid Email Address...\n")
                    print("Strong Email Address...\n")

                else:
                    print("Too Weak to be an Email Address...\n")

            elif re.match(pattern_1, mail):
                if find:
                    print("Valid Gmail Address...\n")
                    print("Strong Gmail Address...\n")

                else:
                    print("Too Weak to be a Gmail Address...\n")

            elif search:
                if find:
                    print("Valid {0}-mail Address...\n".format(find.group('type').upper()))
                    print("Strong {0}mail Address...\n".format(find.group('type').upper()))

                else:
                    print("Too Weak to be a/an {0}mail Address...\n".format(find.group('type').upper()))
                    

            else:              
                print("Invalid Email/Gmail Address...")
                print("Thank you for using the mail validation system")
                break
            
        except AttributeError:
            raise ValueError("Unable to capitalize non-mail...\nEmail;;;=={0}{1}@mail.com"
                                    .format(search.group('upper'), search.group('nums')))
            pass
             
    






