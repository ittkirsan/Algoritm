'''Реализация множества на основе стандартного списка. '''


class PowerSet:
    '''Класс представления множества.'''

    def __init__(self):
        '''Инициализация множества на основе спискаю'''
        self.powerset = []

    def size(self):
        '''Метод определения длинны множества'''
        # количество элементов в множестве
        return len(self.powerset)

    def put(self, value):
        '''Метод сохранения значения в множестве если его нет.'''
        if self.get(value) is False:
            self.powerset.append(value)

    def get(self, value):
        '''Метод определения если данное значения в множестве'''
        # возвращает True если value имеется в множестве,
        # иначе False
        if value in self.powerset:
            return True
        return False

    def remove(self, value):
        '''Метод удаления значения из множества.'''
        # возвращает True если value удалено
        # иначе False
        if self.get(value):
            self.powerset.remove(value)
            return True
        return False

    def intersection(self, set2):
        '''Метод возвращает те значения которые имеются в двух множествах. '''
        # пересечение текущего множества и set2
        power_set = PowerSet()
        for elem in self.powerset:
            if set2.get(elem):
                power_set.put(elem)
        return power_set

    def union(self, set2):
        '''Метод возвращает объеденение двух множеств.'''
        # объединение текущего множества и set2
        power_set = PowerSet()
        for i in self.powerset:
            power_set.put(i)
        for j in set2.powerset:
            power_set.put(j)
        return power_set

    def difference(self, set2):
        ''' Метод возвращается подмножество текущего множества из таких элементов,
         которые не входят в множество-параметр'''
        # разница текущего множества и set2
        power_set = PowerSet()
        for i in self.powerset:
            if set2.get(i) is False:
                power_set.put(i)
        return power_set

    def issubset(self, set2):
        '''Метод роверяет входит ли одно множесто в другое.'''
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        for elem in set2.powerset:
            if self.get(elem) is False:
                return False
        return True
