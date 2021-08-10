class CustomDictionary:
    def __init__(self):
        self._size = 0
        self.keys = []


        



    def __str__(self):
        if self._size == 0:
            return "{}"
        else:
            out_string = "{"
            for i in range(self._size):
                pass

    def __len__(self):
        return self._size