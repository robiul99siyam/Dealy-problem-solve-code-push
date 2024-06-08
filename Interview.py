class stack:
    
    def __init__(self):
        self.items = []
    

    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
        
    def is_empty(self):
        return len(self.items)==0
    
    def display(self):
        print("stack of item display : ",self.items)


s = stack()
s.push(10)
s.push(20)
s.push(30)
# s.push(40)
# s.push(50)
s.pop()
s.display()