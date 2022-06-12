#面向對象相關知識
#三大支柱：封裝、繼承、多態

#例子：工資結算系統。

"""
月薪結算系統 - 部門經理每月15000 程序員每小時200 銷售員1800底薪加銷售額5%提成
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """員工(抽像類)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """結算月薪(抽象方法)"""
        pass


class Manager(Employee):
    """部門經理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序員"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """銷售員"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory:
    """創建員工的工廠（工廠模式 - 通過工廠實現對象使用者和對象之間的解耦合）"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """創建員工"""
        all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
        cls = all_emp_types[emp_type.upper()]
        return cls(*args, **kwargs) if cls else None


def main():
    """主函數"""
    emps = [
        EmployeeFactory.create('M', '曹操'), 
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85), 
        EmployeeFactory.create('S', '典韋', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}: {emp.get_salary():.2f}元')


if __name__ == '__main__':
    main()