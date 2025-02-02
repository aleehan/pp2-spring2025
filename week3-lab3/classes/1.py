class firstClass:
    def getString(self):
        self.s = input("Write your string: ")

    def printString(self):
        self.s = print(self.s.upper())

obj = firstClass()
obj.getString()
obj.printString()

