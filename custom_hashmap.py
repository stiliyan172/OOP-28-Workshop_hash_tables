class HashTable:
    def __init__(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return

        if self.max_capacity == self.size():
            self.__resize()
        index = self.__calc_index(key)
        index = self.__get_index(index)
        self.__keys[index] = key
        self.__values[index] = value

    def __calc_index(self, key):
        index = sum([ord(char) for char in key]) % self.max_capacity
        return index

    def __get_index(self, index):
        if index == self.max_capacity:
            index = 0
        if self.__keys[index] is None:
            return index
        return self.__get_index(index + 1)

    def size(self):
        return len([el for el in self.__keys if el is not None])

    def add(self, key, value):
        self[key] = value

    def __resize(self):
        self.__keys = self.__keys + [None] * self.max_capacity
        self.__values = self.__values + [None] * self.max_capacity
        self.max_capacity *= 2

    def __str__(self):
        keys_values = [f"{self.__keys[index]}: {self.__values[index]}"
                       for index in range(len(self.__keys))
                       if self.__keys[index] is not None]
        return "{ " + ", ".join(keys_values) + " }"

    def get(self, key, default=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return default

    def __len__(self):
        return self.max_capacity


table = HashTable()

table["name"] = "Peter"
table["age"] = 25
table["is_pet_owner"] = True
table["weight"] = 100
table["some"] = "Test"
table["name"] = "Ines"
table.add("new key", "some val")
print(table)
print(table.get("asd"))
print(table["age"])
print(len(table))
