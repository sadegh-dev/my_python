
class Person :
    def __init__(self, name, national_code):
        self.name = name
        self.national_code = national_code

    def __eq__(self,other):
        if isinstance(other, self.__class__):
            return self.national_code == other.national_code
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.national_code != other.national_code
        return False


p1 = Person('charlie', '111111')
p2 = Person('katty', '111111')

print(p1 == p2)