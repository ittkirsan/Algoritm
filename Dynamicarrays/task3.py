'''
Программа реализации динамического массива.
Дмитриевич Вячеслав
'''
import ctypes


class DynArray:
    '''Класс представления динамического массива.'''

    def __init__(self):
        '''Устанавливает все необходимые атрибуты для динамического массива.'''
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        '''Метод вычесления длинны Dynarray. Возвращает число count.'''
        return self.count

    def make_array(self, new_capacity: int):
        '''Формирование блока памяти.'''
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        '''Метод меняющий размер емкости буфера массива.'''
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        '''Метод добавляет элемент в конец массива.'''
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        '''Метод добавляет объект itm в позицию i, начиная с 0.'''
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            self.resize(2*self.capacity)

        if i == self.count:
            self.array[self.count] = itm
            self.count += 1
        else:
            k = self.count
            while k > i:
                self.array[k] = self.array[k-1]
                k -= 1
            self.array[k] = itm
            self.count += 1

    def delete(self, i):
        '''Метод удаляее объект в позиции i.'''
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for j in range(self.count-1):
            if j >= i:
                self.array[j] = self.array[j+1]
        self.count -= 1
        if self.count < self.capacity * 0.5:
            new_capacity = int(self.capacity/1.5)
            if new_capacity < 16:
                self.resize(16)
            else:
                self.resize(new_capacity)
