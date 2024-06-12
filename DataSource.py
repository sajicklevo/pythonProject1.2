class DataSource:
    def fetch_data(self):
        pass

class Base:
    def fetch_data(self):
        print("a")

class File:
    def fetch_data(self):
        print("b")

class Network:
    def fetch_data(self, c):
        print(c)