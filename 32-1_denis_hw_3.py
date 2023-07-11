class Computer:
    def __init__(self,cpu,memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value


    def make_computations(self):
        return self.__memory + self.__cpu

    def __str__(self):
        return f'CPU: {self.__cpu}\nMEMORY: {self.__memory}'

    def __eq__(self, other):
        if isinstance(other,Computer):
            return self.__memory == other.__memory

    def __ne__(self, other):
        if isinstance(other,Computer):
            return self.__memory != other.__memory

    def __lt__(self, other):
        if isinstance(other,Computer):
            return self.__memory < other.__memory

    def __gt__(self, other):
        if isinstance(other,Computer):
            return self.__memory > other.__memory

    def __le__(self, other):
        if isinstance(other,Computer):
            return self.__memory <= other.__memory

    def __ge__(self, other):
        if isinstance(other,Computer):
            return self.__memory >= other.__memory
class Phone:
    def __init__(self,sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self,sim_card_number,call_to_number):
        sim_card = self.__sim_cards_list[sim_card_number - 1]
        print(f'Идет звонок на номер {call_to_number} с сим-карты - {sim_card_number} - {sim_card}')

    def __str__(self):
        return f'SIM CARD LIST: {self.__sim_cards_list}'


class SmartPhone(Computer,Phone):
    def __init__(self,cpu,memory,sim_cards_list):
        Computer.__init__(self,cpu, memory)
        Phone.__init__(self,sim_cards_list)
    def use_gps(self,location):
        print(f'Проложен маршрут от вашего '
              f'местоположения до {location}')

    def __str__(self):
        return f'{Computer.__str__(self)} \n{Phone.__str__(self)}'

print('COMPUTER:')
computer1 = Computer(5,2)
computer2 = Computer(5,7)

print(computer1 == computer2)
print(computer1 != computer2)
print(computer1 <= computer2)
print(computer1 >= computer2)
print(computer1 < computer2)
print(computer1 > computer2)

print(computer1.make_computations())
print(computer1)
print('-------------------')

print('PHONE: ')
phone1 = Phone(['Beeline', 'MegaCom'])
phone1.call(1,'+996556501561')
print('-------------------')

print('SMARTPHONE: ')
smartphone1 = SmartPhone('2.8 GHz',8,['Beeline','O!'])
smartphone1.call(2,"+996567412323")
smartphone1.use_gps('Бишкек')
print(smartphone1)
print('---------------------')

smartphone2 = SmartPhone('4 GHz',12,['MegaCom','O!'])
smartphone2.call(1,"+996555099333")
smartphone2.use_gps('Ош')
print(smartphone2)






