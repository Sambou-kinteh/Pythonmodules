#a dictionary of english letters and their numbers
'''
ENCRYPT_DICT = {0 : 'A',
               1 : 'B',
               2 : 'C',
               3 : 'D',
               4 : 'E',
               5 : 'F',
               6 : 'G',
               7 : 'H',
               8 : 'I',
               9 : 'J',
               10 : 'K',
               11 : 'L',
               12 : 'M',
               13 : 'N',
               14 : 'O',
               15 : 'P',
               16 : 'Q',
               17 : 'R',
               18 : 'S',
               19 : 'T',
               20 : 'U',
               21 : 'V',
               22 : 'W',
               23: 'X',
               24 : 'Y',
               25 : 'Z'}

DECRYPT_DICT = {'A' : 0,
               'B' : 1,
               'C' : 2,
               'D' : 3,
               'E' : 4,
               'F' : 5,
               'G' : 6,
               'H' : 7,
               'I' : 8,
               'J' : 9,
               'K' : 10,
               'L' : 11,
               'M' : 12,
               'N' : 13,
               'O' : 14,
               'P' : 15,
               'Q' : 16,
               'R' : 17,
               'S' : 18,
               'T' : 19,
               'U' : 20,
               'V' : 21,
               'W' : 22,
               'X': 23,
               'Y' : 24,
               'Z' : 25}
'''

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
translated = ' '

#<_______________PATH_WAY sTARTS____________________>
'''                                                                                                                                                  |
#then i will aask for an input in english AND  a SECRET KEY                                               |
#then use my formular                                                                                                             |
#then make a loop to get the dictionary value of the returned key                                          |
#lastly print accordingly the values with a loop, maybe usnig a list of just hard coding:;:;  |        later use.
'''
#<_______________PATH_WAY eNDS______________________>
error = False

while(error == False):
      try:
            print('\rType exit in the message entry to exit\r\n')
            MESSAGE = input('\nEnter Your Message(In English to be Encrypted)\n')#text in enlish to be encrypt
            if MESSAGE.lower() == "exit":
                  break
            
            SECRET_KEY_NUMBER = int(input('\nInput Your secret Key number for encryption: '))
            #error == True
            break
      except ValueError:
            print('Only integer or Number required from 0-25 which is secret to only you(Retry Please)\n')
            error == False

      
class Cipher:
      def __init__(self, message, key, mode = 'encrypt'):
            message = message.upper()
            translated = ' '

            for symbol in message:
                  if symbol in LETTERS:                        
                        num = LETTERS.find(symbol)
                        if mode == 'encrypt':
                              num += key
                        elif mode == 'decrypt':
                              num -= key                              
                        if num >= len(LETTERS):
                              num -= len(LETTERS)
                        elif num < 0:
                              num += len(LETTERS)                              
                        translated += LETTERS[num]
                  else:
                        translated += symbol

            print('Crypted(%d):   %s' %(key, translated))

      #<_________For the transposition CLS_____________>
      def TransEncrypt(message, key):
                  ciphertext = [''] * key

                  for col in range(key):
                        pointer = col
                        while pointer < len(message):

                              ciphertext[col] += message[pointer]
                              pointer += key
                  return ''.join(ciphertext)
                              
      def TransDecrypt(message, key):
                  import math
                  
                  numOfColumns = math.ceil(len(message) / key)
                  numOfRows = key
                  numOfShadedBoxes = (numOfColumns * numOfRows) - len(message) 
                  plaintext = [''] * numOfColumns

                  col = 0
                  row = 0

                  for symbol in message:
                        plaintext[col] += symbol
                        col += 1
                        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes): 
                              col = 0 
                              row += 1
                                                     
                  return ''.join(plaintext)
      #<_______________Transposition ENDS______________>

      def _Encryptor(message, key_no):
            translated = ' '
            for symbol in message:
                  if symbol in LETTERS:                        
                        num = LETTERS.find(symbol)
                        num += key_no
                        
                        if num >= len(LETTERS):
                              num -= len(LETTERS)
                        elif num < 0:
                              num += len(LETTERS)
                              
                        translated += LETTERS[num]

                  else:
                        translated += symbol                        
            print('Encrypted(%d):   %s' %(key_no, translated))


      def _Decryptor(message, key_no):
            translated = ' '
            for symbol in message:
                  if symbol in LETTERS:                        
                        num = LETTERS.find(symbol)
                        num -= key_no
                        
                        if num >= len(LETTERS):
                              num -= len(LETTERS)
                        elif num < 0:
                              num += len(LETTERS)
                              
                        translated += LETTERS[num]

                  else:
                        translated += symbol
            print('Decrypted(%d):   %s' %(key_no, translated))

class  TransposeFile(Cipher):
      def __init__(self, file, key, mode = 'encrypt'):
            import time, os, sys, Deleting_Files
            
            startime = time.time()
            actual_file_name = os.path.basename(file)
            crypted_extension_split = os.path.splitext(actual_file_name)
            crypted_extension = crypted_extension_split[0] + '.%sed'.lower() %(mode.title()) + crypted_extension_split[1]

            self.file = file
            self.key = key
            self.mode = mode
            if not os.path.exists(file):
                  print(' The Input file %s does not exist. Quitting...' % (file))
                  sys.exit()
            if os.path.exists(file):
                  print('This will override the current content of file(%s)(C)ontiue or (Quit)?'%(actual_file_name))
                  res = input('> ')
                  if not res.lower().startswith() == 'c':
                        sys.exit()

            print('%sing...'.capitalize() %(mode.title()))
            with open(self.file, 'r') as msg:
                  text = ''
                  for i in msg:
                        text += ''.join(i)
                  if mode == 'encrypt':
                        #print('\n',Cipher.TransEncrypt(text, self.key))
                        new_path_split = os.path.splitext(self.file)
                        new_path = new_path_split[0] + '.%s'.lower() %(mode.title()) + new_path_split[1]
                        op = open(new_path, 'w')
                        op.write(Cipher.TransEncrypt(text, self.key))
                        print('Done %sing %s (%d Characters). '%(mode.title(), actual_file_name, (len(text))))
                        print('Encrypted file is %s' %(crypted_extension))
                        print('%sion time:  %ss' %(mode.title(), round(time.time() - startime, 2)))
                        msg.close()
                        op.close()
                        
                  elif mode == 'decrypt':
                        #print('\n',Cipher.TransDecrypt(text, self.key))
                        new_path_split = os.path.splitext(self.file)
                        new_path = new_path_split[0] + '.%s'.lower() %(mode.title()) + new_path_split[1]
                        op = open(new_path, 'w')
                        op.write(Cipher.TransDecrypt(text, self.key))
                        print('Done %sing %s (%d Characters). '%(mode.title(), actual_file_name, (len(text))))
                        print('Decrypted file is %s' %(crypted_extension))
                        print('%sion time:  %ss' %(mode.title(), round(time.time() - startime, 2)))
                        msg.close()
                        op.close()
                  Deleting_Files.Sam_D(file)
                        
            
if __name__ == '__main__':
      while(True):
            choice = input('\nDo you want to decrypt or encrypt this message(d/e): ')
            print('\n')
            if choice == 'e' or  choice == 'encrypt':
                  Cipher._Encryptor(MESSAGE, SECRET_KEY_NUMBER)
                  break
            elif choice == 'd' or  choice == 'decrypt':
                  Cipher._Decryptor(MESSAGE, SECRET_KEY_NUMBER)
                  break
            else:
                  print('\nInvalid OPTION')



                  
                  
                  






