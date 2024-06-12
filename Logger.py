class Logger(ABC):
    @abstractmethod
    def log(self,message):
        pass
class ConsoleLogger(Logger):
    def log(self,message):
        print(message)
class FileLogger(Logger):
    def log(self,message):
        with open('log.txt''w')as f:
            f.write(message)
            f.close()
class EmailLogger(Logger):
    def log(self,message):
        with open('log''w')as f:
            f.write(message)
            f.close()
console_l=ConsoleLogger()
file_l=FileLogger()
email_l=EmailLogger()
console_l.log('hello')
file_l.log('hello')
email.log('hello')