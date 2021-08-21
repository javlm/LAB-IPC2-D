class Letter():
    def __init__(self, num, char):
        self.num = num
        self.char = char
        self.siguiente = None
        self.anterior = None

    def setAttr(self, *attr):
        self.num = attr[0]
        self.char = attr[1]


