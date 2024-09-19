class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя {self.__engine_power} л/с'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
    def set_color(self, set_color):
        if set_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = set_color
        else: print(f'Нельзя сменить цвет на {set_color}')

class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5
    def __init__(self, owner, model, engine_power, color ):
        super().__init__(owner, model, engine_power, color)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства

vehicle1.print_info()

#Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

