class rdp:
    def __init__(self, S):
        self.input = S.replace(" ", "")  # remove spaces
        self.index = 0 #input buffer pointer 

    def match(self,char):
         
        if self.input[self.index] == char:
            self.index +=1
            return True
        return False

    #checking for S production 
    def S(self):
        if self.match('a'):
            return True
        elif self.match('('):
            if self.L():
                if self.match(')'):
                    return True
            return False
        return False

    #checking for L PRODUCTION 
    def L(self):
        if self.S():
            return self.L_dash()
        return False

   #checking for L' PRODUCTION 
    def L_dash(self):
        if self.match(','):
            if self.S():
                return self.L_dash()
            return False
        return True   

    def parse(self):
        if self.S():
            return "Valid string"
        return "Invalid string"



S = input("Enter string: ")
parser = rdp(S)
print(parser.parse())