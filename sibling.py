#------------IN PYTHON PL----------=

import sys

def sibling():
    while(True):
        print("How many siblings does paulo have")
        answer = sys.stdin.readline()
        answer = int(answer)

        if (answer != 12):
            print("Incorrect! Try again\n")

        else:
            print("You are Correct!!!\n")
            break

if __name__ == '__main__':
    sibling()

#but
#-----------------IN KOTLIN PL(Native jave framework)----------------#
'''
fun main(args: Array<String>){

	//set our local variable
	//val numsibs: Int? = 12
	var isTrue: Boolean? = false

	do{
		println("How many siblings does Paulo have")
		var answer: Int? = readLine()!!.toInt()

		when(answer){
			12 -> {println("You are Correct!!!\n")
				isTrue = true	

			}else{
				println("Incorrect! Try again\n")

			}

		}
	

	}while(isTrue == false)



}

'''




















