class Book:
    def __init__(self,read,write,info):
        self.read=read
        self.write=write
        self.info=info
class Novel(Book):
    def __init__(self,read,write,info,plot,subject):
        super().__init__(read,write,info)
        self.plot=plot
        self.subject=subject
        self.read=read
        self.write=write
        self.info=info
        self.plot=plot
        self.subject=subject
class TextBook(Book):
    def __init__(self,read,write,info,subject,plot,):
        super().__init__(read,write,info)
        self.subject=subject
        self.read=read
        self.write=write
        self.info=info
        self.subject=subject
        self.plot=plot
novel=Novel(read=True,write=True,info=True,plot=True,subject=True)
print(novel.read)
print(novel.write)
print(novel.info)
print(novel.plot)
print(novel.subject)
textbook=TextBook(read=True,write=True,info=True,subject=True,plot=True)
print(textbook.read)
print(textbook.write)
print(textbook.info)
print(textbook.subject)
print(textbook.plot)