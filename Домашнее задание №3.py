class Computer:
    def __init__(self, cpu, memory):
        self.__cpu=cpu
        self.__memory=memory
    
    def __make_computations(self):
        return f"""{self.__cpu} + {self.__memory} = {self.__cpu + self.__memory}
{self.__cpu} - {self.__memory} = {self.__cpu - self.__memory}
{self.__cpu} * {self.__memory} = {self.__cpu * self.__memory}
{self.__cpu} / {self.__memory} = {self.__cpu / self.__memory}"""
        
    def cpu_get_coort(self):
        return self.__cpu
    
    def memory_get_coort(self):
        return self.__memory
    
    def info(self):
        computer = Computer(9,1)
        laptor = Laptop(5,512,64)
        print(f"""Компьютер:
Процессор - INTEL Core {computer.cpu_get_coort()}
Память - SSD {computer.memory_get_coort()}TB
Ноутбук:
Процессор - INTEL Core {laptor.cpu_get_coort()}
Память - SSD {laptor.memory_get_coort()}GB
Карта памяти - MicroSDXC {laptor.memote_card_get_coort()}GB
Арифметические вычисление:
{computer.__make_computations()}
{laptor.__make_computations()}""")
    
class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card=memory_card

    def memote_card_get_coort(self):
        return self.__memory_card
Computer.info(True)
