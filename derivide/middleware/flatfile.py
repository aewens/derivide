from json import dumps as json_dumps, loads as json_loads
from pickle import dumps as pkl_dumps, loads as pkl_loads

from pathlib import Path

modes = ["json", "pickle"]

class DerivideFlatFile:
    def __init__(self, path, mode="json"):
        assert mode in modes, f"Invalid mode: {mode}"
        self.path = Path(path).resolve()
        self.mode = mode
        self.data = dict()


    def read(self):
        with open(self.path, "rb") as flatfile:
            raw_data = flatfile.read()
            if self.mode == "json":
                self.data = json_loads(raw_data.decode())

            elif self.mode == "pickle":
                self.data = pkl_loads(raw_data)

        return self.data

    def write(self, data=None):
        if data is None:
            data = self.data

        with open(self.path, "wb") as flatfile:
            if self.mode == "json":
                encoded = json_dumps(data).encode()

            elif self.mode == "pickle":
                encoded = pkl_dumps(data)

            flatfile.write(encoded)

    def start(self):
        if not self.path.exists():
            self.write()

        self.read()

    def save(self):
        self.write()

    def all(self):
        return self.read()

    def get(self, *entry_path):
        pointer = self.data
        for entry in entry_path:
            if pointer is None:
                return None

            if isinstance(entry, str) and isinstance(pointer, dict):
                pointer = pointer.get(entry)

            elif isinstance(entry, int) and isinstance(pointer, list):
                if entry < 0 and entry >= len(pointer):
                    return None

                pointer = pointer[entry]

            else:
                return None

        return pointer

    def put(self, *entry_path, value):
        *entries, key = entry_path
        pointer = self.get(*entries)
        if pointer is None:
            return False

        if isinstance(key, str) and isinstance(pointer, dict):
            pointer[key] = value

        elif isinstance(key, int) and isinstance(pointer, list):
            if key != len(pointer):
                return False

            pointer.append(value)

        else:
            return False

        return True

    def drop(self, *entry_path):
        *entries, key = entry_path
        pointer = self.get(*entries)
        if pointer is None:
            return False

        if isinstance(key, str) and isinstance(pointer, dict):
            pointer.pop(key, None)

        elif isinstance(key, int) and isinstance(pointer, list):
            if key < 0 and key >= len(pointer):
                return False

            pointer.pop(key)

        else:
            return False

        return True
