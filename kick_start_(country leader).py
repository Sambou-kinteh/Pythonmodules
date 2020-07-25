import sys

#taking the standard input and removing the newlines recorded
INPUT = sys.stdin.readlines()
inputCorrection = [ i.replace('\n', '') for i in INPUT]

try:
    allNum = []
    for i in inputCorrection:
        if int(type(i)) == int:
            allNum.append(i)         

except:
    pass

print(allNum)
        

try:
    #constants and limits
    T = int(inputCorrection[0])
    N = int(inputCorrection[1])
    lastGuy = N + 2
    if str(T).isalnum and str(N).isalnum:
        if T and N > 100:
            print("Limit Exceeded")

        else:
            pass
            '''if T == 1:
                allPersons = inputCorrection[2 : lastGuy]

            elif T > 1:
                #cases = [ eachCase for eachCase in inputCorrection]
                firstCase =  inputCorrection[0:lastGuy]
                print(firstCase)
                
                secondPersonNo = int(inputCorrection[lastGuy])
                secondCase = inputCorrection[lastGuy : (lastGuy+1) + secondPersonNo]
                print(secondCase)'''

            for eachTestSet in range(T):
                allNum = [ i.isalnum for i in inputCorrection]
                    
                #to be continued
                
            

except ValueError:
    sys.stdout.write("Invalid Input in line 1 or 2")
    
    
    












    
#sys.stdout.write(sam)
#crlt-d to take in the input
