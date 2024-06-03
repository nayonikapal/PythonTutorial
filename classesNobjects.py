class HumanBeing:
    def human(self,nxt=None):
        return f"This is testing Function {nxt}"
    
obj = HumanBeing()
print(obj.human(": Ujjwal :"))

print(HumanBeing.human(obj,": Ujjwal :"))