class Basic:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Basic - name: %s"%self.name)

obj1=Basic('Apricot')
obj1.show()

dir(Basic)

dir(obj1)

class Basic1(object):
    pass
