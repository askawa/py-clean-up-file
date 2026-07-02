import os
from pytest import File


class CleanUpFile:
    def __init__(self, filename) -> None:
        self.filename = filename

    def __enter__(self) -> File:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return False
