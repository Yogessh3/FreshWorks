class NodeValue:
    def __init__(self,value):
        self.value=value
class DataStore:
    def __init__(self):
        self.data={}
    def create(self,key,value):
        if key in self.data:
            return False
        val=NodeValue(value)
        self.data[key]=val
        return True
    def read(self,key):
        if key in self.data:
            valueObj=self.data[key]
            return valueObj.value
        else:
            return False
    def delete(self,key):
        if key in self.data:
            del self.data[key]
            return True
        else:
            return False
Dts=DataStore()
Dts.create("A",1)
Dts.create("B",2)
Dts.create("C",3)
Dts.create("D",4)
print(Dts.create("A",1))
print(Dts.read("A"))
print(Dts.read("B"))
print(Dts.read("C"))
print(Dts.delete("C"))
