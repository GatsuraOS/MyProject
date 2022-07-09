# Создать класс, описывающий человека с атрибутами имени, фамилии
# возраста.
# Реализовать магический метод str
# добавить атрибут grades в котором будет хранится список оценок
# реализовать сравнение объектов данного класса на основании среднего
# арифметического оценок
# реализовать property для атрибута grades чтобы выводило не список, а
# среднее арифметическое


class Student:

    def __init__(self, first_name: str, last_name: str, age: int, grades: list) -> None:
        self._grades = grades
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        return f"Student({self.first_name=} {self.last_name=} {self.age=})"

    @property
    def grades(self):
        return self.__average(self)

    def __average(self, other) -> float:
        return round(sum(other._grades) / len(other._grades), 2)

    def __gt__(self, other):
        return self.__average(self) > self.__average(other)

    def __lt__(self, other):
        return self.__average(self) < self.__average(other)

    def __ge__(self, other):
        return self.__average(self) >= self.__average(other)

    def __le__(self, other):
        return self.__average(self) <= self.__average(other)

    def __eq__(self, other):
        return self.__average(self) == self.__average(other)

    def __ne__(self, other):
        return self.__average(self) != self.__average(other)


vasya = Student("vasya", "vaskin", 15, [2, 3, 2, 2, 3, 4])
petya = Student("petya", "petkin", 16, [4, 5, 3, 4])
print(vasya.grades)
print(petya.grades)
print(vasya <= petya)