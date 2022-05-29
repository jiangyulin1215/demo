"""Jyl 代码编写"""


class Car():
    def __init__(self, number, brand):
        # self.name = name
        self.number = number
        self.brand = brand

    def start(self):
        pass

    def stop(self):
        pass

    def show(self):
        # print(f'我是{self.name},我的车牌是{self.number}')
        pass


class Taxi(Car):
    def __init__(self, company, number, brand):
        super(Taxi, self).__init__(number, brand)
        self.company = company

    def start(self):  # 子类重写父类方法
        print(f'我是{self.company}公司的，我的车牌号是{self.number},品牌是{self.brand}')

    def stop(self):  # 子类重写父类方法
        print('乘客您好，目的地导了')

    def show(self):
        pass


class Private_Car(Car):
    def __init__(self, name, number, brand):
        super(Private_Car, self).__init__(number, brand)
        self.name = name

    def start(self):
        print(f'我是{self.name},出发，自己家的车牌是{self.number}')

    def stop(self):
        print('到了，下车')

    def show(self):
        pass


if __name__ == '__main__':
    taxi = Taxi('上海大众', '京A 88888', '长城')
    # print(Taxi.start())
    taxi.start()
    taxi.stop()
    taxi.show()
    # print(taxi)
    # print(Taxi)

    private_car = Private_Car('张三', '京A 99999', '本次')
    private_car.start()
    private_car.stop()
