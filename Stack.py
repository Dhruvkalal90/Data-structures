"""I confirm that the code provided here was written entirely by myself,
without any assistance from external sources or individuals.
I did not rely on any pre-existing templates, online resources,
or third-party help in the creation of this code. The logic, structure,
and implementation are all the result of my own work and understanding."""
import time
class Stack:
    def __init__(self,size=5):
        self.top=-1
        self.max=size-1
        self.stack=[0]*size
    def push(self,val):
        if self.top>=self.max:
            print("Stack is full")
        else:
            self.top += 1
            self.stack[self.top]=val
    def pop(self):
        if self.top<0:
            print("Stack is empty")
        else:
            self.stack[self.top]=0
            self.top-=1
    def __str__(self):
        return str(self.stack[:self.max+1])
    def peek(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print(self.stack[self.top])
    def size(self):
        size=self.max+1
        print(size)
        return size
    def is_full(self):
        if self.top>=self.max:
            return True
        else:
            return False
    def is_empty(self):
        if self.top==-1:
            return True
        else:
            return False
    def to_list(self):
        li=list(self.stack[:self.top+1])
        return li
    def contains(self,val):
        if self.is_empty and (val in self.stack):
            return True
        else:
            if self.is_empty:
                print("Stack is empty")
            return False
    def clear(self):
        self.top=-1
        for val in range(0,self.max+1):
            self.stack[val]=0


s=Stack(10)#Creates stack of 10 size. Default is 5
while True:
    print("\n\n1. push\n2. pop\n3.peek\n4.size\n5.is_full\n6. is empty\n7.to list\n8. contains\n9. clear\n10 Show stack\n11. to end")
    choice=int(input("Enter your choice:"))
    if choice==1:
        inp=int(input("Enter number:"))
        s.push(inp)
        time.sleep(1)
    elif choice==2:
        s.pop()
        time.sleep(1)
    elif choice==3:
        s.peek()
        time.sleep(1)
    elif choice==4:
        print(s.size())
        time.sleep(1)
    elif choice==5:
        print(s.is_full())
        time.sleep(1)
    elif choice==6:
        print(s.is_empty())
        time.sleep(1)
    elif choice==7:
        print(s.to_list())
        time.sleep(1)
    elif choice==8:
        check = int(input("Enter number to check:"))
        print(s.contains(check))
        time.sleep(1)
    elif choice==9:
        s.clear()
        time.sleep(1)
    elif choice==10:
        print(s)
        time.sleep(1)
    elif choice==11:
        print("Thank You")
        time.sleep(1)
        break
    else:
        print("Invalid choice!")
        time.sleep(1)
        continue