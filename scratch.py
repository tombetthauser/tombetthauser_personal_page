class Map:
    def __init__(self):
        self.table = []
        for i in range(8):
            self.table.append([])

    def _hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum

    # upsert = instert and/or update
    def insert(self, key, val):
        hash = self._hash(key)
        bucket = self.table[hash % len(self.table)]
        for i in range(len(bucket)):
            bucket_key, _ = bucket[i]
            if key == bucket_key:
                bucket[i] = (key, val)
                return
        bucket.append((key, val))

    def get(self, key):
        hash = self._hash(key)
        bucket = self.table[hash % len(self.table)]
        for i in range(len(bucket)):
            bucket_key, bucket_val = bucket[i]
            if key == bucket_key:
                return bucket_val
        raise ValueError(f"{key} not found dipshit")

    def has(self, key):
        hash = self._hash(key)
        bucket = self.table[hash % len(self.table)]
        for i in range(len(bucket)):
            bucket_key, bucket_val = bucket[i]
            if key == bucket_key:
                return True
        return False

my_map = Map()
my_map.insert("doggies", 15)
my_map.insert("doggies", 7)
my_map.insert("cats", 25)
print(my_map.get("doggies"))
print(my_map.get("cats"))
# print(my_map.get("cats"))
for ele in my_map.table:
  print(ele)
