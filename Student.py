class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    # Getter for name
    # @property
    # def name(self):
    #     return self._name

    # # Setter for name
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Invalid name")
    #     self._name = name

    # @property
    # def house(self):
    #     return self._house

    # @house.setter
    # def house(self, house):
    #     if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    #         raise ValueError("Invalid house")
    #     self._house = house


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
