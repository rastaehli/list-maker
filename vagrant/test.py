class Demo(object):
    def __init__(self, name):
        self.name = name

    def addLast(self, l):
        self.name = self.name+l
        return self

d = Demo('Richard'
	).addLast( 
		' Alan'
	).addLast( 
		' Staehli')

print(d.name)
