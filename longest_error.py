"""

class parent(object):
    def __init__(self, something):
        self.something = something
        
        


class child(parent):
    def __init__(self,anotherthing = 0):
        super().__init__(self)
        #super(child, self).__init__(something)
        #self.anotherthing = anotherthing
        #self.something = something

#parent("kk")
child()


"""


import excel_automated_working as el

print(el.sama["sam"])
el.modObj

