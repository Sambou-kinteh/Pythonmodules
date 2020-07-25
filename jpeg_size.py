
def JpegSize(file_name):
          '''This function prints the resolution of the jpeg image file
               passed into it'''
          with open(file_name, 'rb') as img_file:

               #height of image (in 2 bytes) is at 164th position
               img_file.seek(163)
               #read the 2 bytes
               
               a = img_file.read(2)
               height = (a[0] << 8) + a[1]
               #next 2 bytes in width
               a = img_file.read(2)
               width = (a[0] << 8) + a[1]
          while(True):
               return print("\nSize: %s x %s" % (width, height))               
               
     
