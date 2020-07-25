
class SpecialString:

    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont

            result += ">" + other.cont[index:]
            print(result)


    def __lt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[index:] + ">" + self.cont

            result += ">" + other.cont[:index]
            print(result)

'''
foo = SpecialString("foo")
bar = SpecialString("bar")

foo > bar
foo < bar
'''
