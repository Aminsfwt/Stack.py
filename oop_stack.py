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


stack_1 = stack()
stack_2 = stack_ver2()

#print(stack.__dict__)



stack_2.push(20)
stack_2.push(20)
stack_2.push(20)
stack_2.push(20)
stack_2.push(20)


stack_2.pop()
stack_2.pop()
stack_2.pop()
stack_2.pop()
stack_2.pop()
stack_2.pop()
stack_2.push(20.25)
stack_2.push(2.2352)
#stack_2.push(20)
#x = stack_2.pop()
Summs = stack_2.stack_sum()
print(f"The sum of the data in the stack = {Summs}")

print(f"The number of the elements in the stack = {stack_2.size_of_stack}")

"""
for i in range(5):
    stack_2.push(i*20)
    print(f"the sum of data in the stack = {stack_2.stack_sum()}")

print('*'*50)
print(f"the added data = {stack_2.list}")
print(f"the size of list after pushing = {stack_2.size_of_stack}")

print('*'*50)


for i in range(len(stack_2.list)):
    print('*'*50)
    print(f"the removed data = {stack_2.pop()}")
    print(f"the list after remove data = {stack_2.list}")
    print(f"the size of list after removing = {stack.size_of_stack}")

print('*'*50)
print(f"The Second STACK = {stack_2.list}")
print(stack_2.list)

"""




