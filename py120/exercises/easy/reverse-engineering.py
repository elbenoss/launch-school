

class Transform:
    def __init__(self, data):
        self.data = data

    def uppercase(self):
        return self.data.upper()

    @staticmethod
    def lowercase(str_):
        return str_.lower()

"""
    def uppercase(self):
        if isinstance(self, Transform):
            transformed = self.string
        else:
            transformed = self
        return transformed.upper()

    def lowercase(self):
        if isinstance(self, Transform):
            transformed = self.string
        else:
            transformed = self
        return transformed.lower()
"""



my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz
