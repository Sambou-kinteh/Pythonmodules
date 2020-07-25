method = 'In forn Sam_D("Put the file name here")\n'
print(method)

def Sam_D(file_dirr):
      try:
            import time
            import subprocess
            #first use an input
            #second save the dir in a *txt file
            #then run the bat file to delete
            path = 'C:\\Users\\Sambou\\deletion_process.bat'

            #file_dirr = input('Please enter the directory name of the file you wise to delete:\n')

            with open(path, 'w') as dirr:
                  dirr.write('del "%s"' %(file_dirr))
                  dirr.close

            subprocess.Popen(path)
            time.sleep(1)
            print('log: File Deleted(at %s)' %(time.ctime(time.time())))

      except Exception as msg:
            print(msg)
