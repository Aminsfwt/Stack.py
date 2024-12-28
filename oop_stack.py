class stack:            #superclass
    size_of_stack = 0   #class level data

    def __init__(self):
        self.list = []  

    def push(self,data):
        self.list.append(data)
        stack.size_of_stack += 1 
        
    def pop(self):
        k = self.list[-1]
        del self.list[-1]
        stack.size_of_stack -= 1
        return k


class stack_ver2(stack):    #inhereted class
    sum_of_stack = 0        #class level data
    max = 5

    def __init__(self):
        super().__init__()
    
    def push(self, data):
        if (len(self.list) <  stack_ver2.max):
            stack.push(self, data)
            stack_ver2.sum_of_stack += data
        else:
            print("Error, The Stack is full of 5 elements now!!!!")    
       
    def pop(self):
        if(len(self.list) > 0):
            z = stack.pop(self)
            stack_ver2.sum_of_stack -= z
            return z
        else:
            print("Error, The Stack is empty now!!!!")
         
    def stack_sum(self):
        x = stack_ver2.sum_of_stack
        return x


