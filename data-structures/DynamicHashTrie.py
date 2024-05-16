class TrieNode:
    def __init__(self):
        self.children = {}
        self.key_values = []


class DynamicHashTrie:
    def __init__(self, initial_size=16):
        self.buckets = [None] * initial_size
        self.size = 0
        self.load_factor = 0.75

    def _hash(self, key):
        return hash(key) % len(self.buckets)

    def _resize(self, new_size):
        old_buckets = self.buckets
        self.buckets = [None] * new_size
        for bucket in old_buckets:
            if bucket:
                for key, value in bucket.key_values:
                    self.put(key, value)

    def put(self, key, value):
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = TrieNode()
        node = self.buckets[index]

        # Insert or update the key-value pair
        for kv in node.key_values:
            if kv[0] == key:
                kv[1] = value
                return
        node.key_values.append((key, value))
        self.size += 1

        # Check load factor and resize if needed
        if self.size / len(self.buckets) > self.load_factor:
            self._resize(len(self.buckets) * 2)

    def get(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        if node:
            for kv in node.key_values:
                if kv[0] == key:
                    return kv[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        if node:
            for kv in node.key_values:
                if kv[0] == key:
                    node.key_values.remove(kv)
                    self.size -= 1
                    return True
        return False

    def prefix_search(self, prefix):
        results = []
        for bucket in self.buckets:
            if bucket:
                for key, value in bucket.key_values:
                    if key.startswith(prefix):
                        results.append((key, value))
        return results


# Example usage
dht = DynamicHashTrie()
dht.put("apple", 1)
dht.put("app", 2)
dht.put("banana", 3)
print(dht.get("apple"))  # Output: 1
print(dht.prefix_search("app"))  # Output: [('apple', 1), ('app', 2)]
dht.remove("apple")
print(dht.get("apple"))  # Output: None
