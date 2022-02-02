'''Реализация хеш-таблицы'''


class HashTable:
    '''Класс представления хеш-таблицы'''

    def __init__(self, sz: int, stp: int):
        '''Иницилизация хеш-таблицы'''
        self.size = sz   # размер хэш-таблицы
        self.step = stp  # длина шага для поиска следующего свободного слота
        self.__slots = [None] * self.size

    def hash_fun(self, value):
        return sum(value.encode('utf-8')) % self.size

    def seek_slot(self, value):
        '''Поиск слота'''
        index = self.hash_fun(value)
        position_count = index
        iter_count = self.size
        while iter_count >= 0:
            if self.__slots[position_count] == None:
                return position_count
            elif self.__slots[position_count] == value:
                return position_count
            else:
                position_count += self.step
                if position_count > (self.size-1):
                    position_count -= self.size
            iter_count -= 1
        return None

    def put(self, value):
        '''Помещение значения в слот'''
        if self.seek_slot(value) != None:
            self.__slots[self.seek_slot(value)] = value
            return self.seek_slot(value)
        return None

    def find(self, value):
        '''Поиск значение в слоте'''
        find_index = self.seek_slot(value)
        if find_index != None:
            if self.__slots[find_index] == value:
                return find_index
        return None
