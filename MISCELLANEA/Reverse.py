class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopException
        self.index -= 1
        return self.data[self.index]

class B(Exception):
  pass
class C(B):
  pass
class D(C):
  pass

for cls in [B, C, D]:
  try:
    raise cls()
  except D:
    print("D")
  except C:
    print("C")
  except B:
    print("B")
