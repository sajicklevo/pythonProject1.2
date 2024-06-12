class Employee:
    def __init__(self,get_salary,get_position,work):
        self.get_salary=get_salary
        self.get_position=get_position
        self.work=work
class Manager(Employee):
    def __init__(self,get_salary,get_position,work):
        super().__init__(get_salary,get_position,work)
        self.get_salary=get_salary
        self.get_position=get_position
        self.work=work
class Developer(Employee):
    def __init__(self,manage_team,write_code):
        super().__init__(manage_team,write_code,True)
        self.manage_team=manage_team
        self.write_code=write_code
        self.work=True
manager=Manager(1000,'Manager',True)
print(manager.get_salary)
print(manager.get_position)
print(manager.work)
developer=Developer(1000,True,)
print(developer.get_salary)
print(developer.get_position)
print(developer.work)