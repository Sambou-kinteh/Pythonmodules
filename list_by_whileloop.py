
def Punctuation(format_p):
     no_punc = ''
     punc = ''' \|,<.>/?;:'"@#~=+-_)(*&^%$£!¬` '''
     for char in format_p:
          if char not in punc:
               no_punc += char
     return no_punc
     
i = 0
j = 10

for i in range(0,10):
     i += 1
     for j in range(10,20):
          j+= 1
          print(Punctuation(list('[{0}{1}]'.format(i,j))))
