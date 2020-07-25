def count_letters(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count        
try:
    file = input('Enter your files name: ')
    #letter = input('Enter a letter you want to count: ')
    with open(file) as f:
        text = f.read()

    #print(count_letters(text,letter))    
except FileNotFoundError:
    print('\nThis file is not found in the current directory')

for char in "abcdefghijklmnopqrstuvwxyz":
        perc = 100*count_letters(text, char)/len(text)
        print("{0}-{1}%".format(char,round(perc,2)))
    
