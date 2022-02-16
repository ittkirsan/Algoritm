class BloomFilter:
    def __init__(self, f_len):
        # создаём битовый массив длиной f_len ...
        self.filter_len = f_len
        self.bit_array = 0
        self.number_1 = 17
        self.number_2 = 223

    def hash1(self, str1):
        # 17
        hash_index = 0
        for c in str1:
            code = ord(c)
            hash_index = ((3*code+7) % self.number_1) % 32
        return hash_index

    def hash2(self, str1):
        # 223
        hash_index = 0
        for c in str1:
            code = ord(c)
            hash_index = ((3*code+7) % self.number_2) % 32
        return hash_index

    def add(self, str1):
        # добавляем строку str1 в фильтр
        mask = self.hash1(str1) | self.hash2(str1)
        self.bit_array |= mask

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        mask = self.hash1(str1) | self.hash2(str1)
        if (self.bit_array & mask) == mask:
            return True
        return False
