class Person:
    @property
    def name(self):
        return ' '.join(self._name)

    @name.setter
    def name(self, value):
        self._name = value.split()

person = Person()
person.name = '\t Guido  van Rossum \n'
print(person.name)
'Guido van Rossum'