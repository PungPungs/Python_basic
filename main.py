class UiStructure():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        cls = type(self)
        if not hasattr("_init"):
            self.data = 1


a = UiStructure()
b = UiStructure()
c = UiStructure()

print(a)
print(b)
print(c)