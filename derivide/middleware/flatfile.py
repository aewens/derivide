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
        self._ref = None

        self._load()

    def _load(self):
        self.start()
        self._ref.close()

    def read(self):
        self._ref.seek(0)
        raw_data = self._ref.read()
        if self.mode == "json":
            self.data = json_loads(raw_data.decode())

        elif self.mode == "pickle":
            self.data = pkl_loads(raw_data)

        return self.data

    def write(self, data=None):
        if data is None:
            data = self.data

        if self.mode == "json":
            encoded = json_dumps(data).encode()

        elif self.mode == "pickle":
            encoded = pkl_dumps(data)

        self._ref.seek(0)
        self._ref.write(encoded)
        self._ref.truncate()

    def start(self):
        exists = self.path.exists()
        self.path.touch(mode=0o700)
        self._ref = open(self.path, "r+b")
        if not exists:
            self.write()

        else:
            self.read()

    def save(self):
        self.write()
        self._ref.close()

    def reload():
        return self.read()

    def all(self):
        return self.data

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
