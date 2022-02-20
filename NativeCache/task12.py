'''Класс представления структурны данных Кэш.'''


class NativeCache:
    def __init__(self, sz):
        self.size = sz  # размер хэш-таблицы
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.number = 17

    def hash_fun(self, value):
        if not isinstance(value, str):
            return None

        return sum(value.encode('utf-8')) % self.size

    def seek_slot(self, value: str):
        '''Поиск слота'''
        if not isinstance(value, str):
            return None

        index = self.hash_fun(value)
        position_count = index
        iter_count = self.size
        while iter_count >= 0:
            if self.slots[position_count] == None:
                return position_count
            elif self.slots[position_count] == value:
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
            self.slots[self.seek_slot(value)] = value
            return self.seek_slot(value)
        return None

    def is_key(self, key: str):
        '''Метод проверяет емеется ли ключ в слотах.'''
        # возвращает True если ключ имеется,
        # иначе False
        if not isinstance(key, str):
            return None
        if key in self.slots:
            return True
        return False

    def get(self, key):

        if not isinstance(key, str):
            return None
        if self.is_key(key):
            # добавляем новое обращение к ключу
            self.hits[self.slots.index(key)] += 1
            return self.values[self.hash_fun(key)]
        return None

    def put(self, key, value):

        index = self.seek_slot(key)
        if index is not None:    # если есть свободное место или ключ key
            if self.slots[index] == key:
                self.values[index] = value

            else:    # ключа key нет, но есть свободный слот
                self.slots[index] = key
                self.values[index] = value
        else:    # если нет такого ключа или свободных слотов

            self.slots[self.hits.index(min(self.hits))] = key
            self.values[self.hits.index(min(self.hits))] = value
            self.hits[self.hits.index(min(self.hits))] = 0
