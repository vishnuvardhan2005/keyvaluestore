import json
import os

# Key value store implementation
class KeyValueStore:
    def __init__(self, file_path):
        self.store = {}
        self.db_file = file_path
        self.load_from_disk()

    def get(self, key):
        return self.store.get(key, None);

    def set(self, key, value):
        self.store[key] = value;
        self.write_to_disk();

    def remove(self, key):
        if key in self.store:
            del self.store[key];
            self.write_to_disk();

    def load_from_disk(self):
        if os.path.exists(self.db_file) and os.path.getsize(self.db_file) > 0:
            try:
                with open(self.db_file, 'r') as f:
                    self.store = json.load(f)
            except FileNotFoundError:
                self.store = {}
    
    def write_to_disk(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.store, f)
            print("data written to file successfully")


def main():
    store = KeyValueStore("data/cities.db");

    store.set("HYD", "Hyderabad");
    store.set("BANG", "Bangalore");
    print(store.get("HYD"));
    print(store.get("BANG"));

    store.remove("HYD")
    print(store.get("HYD"))
    print(store.get("BANG"))

if __name__ == '__main__':
    main()

