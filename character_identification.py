#first we define our characters bytes table

BYTE_DICT = {'HASH_TAG' : 35,
             'PERCENT_SIGN' : 37,
             'DOLLAR_SIGN' : 36,
             'EURO_SIGN' : 163,
             }

def iden():
      char = input('Enter a character: ')
      for i in BYTE_DICT.values:
            if ord(char) == i:
                  print(hashtag)
iden()
