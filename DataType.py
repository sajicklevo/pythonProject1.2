class DataType(ABC):
    @abstractmethod
    def process(self):
        pass
class Number(DataType):
    def __init__(self,number):
        self.number=number
    def process(self):
        return self.number
class String(DataType):
    def __init__(self,string):
        self.string=string
    def process(self):
        return self.string
class Lists(DataType):
    def __init__(self,list):
        self.list=list
    def process(self):
        return self.list
number=Number(10)
print(number.process())
string=String('hello')
print(string.process())
list=Lists([1,2,3,4,5,6,7])
print(list.process())
