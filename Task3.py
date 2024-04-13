import math


class Point:

    @staticmethod
    def check_coord(x, y):
        if (x not in range(-100, 101)) or (y not in range(-100, 101)):
            raise ValueError("Координаты объекта не попадают в диапозон от -100 до 100")
        else:
            return [x, y]

    def __init__(self, x, y):
        if self.check_coord(x, y):
            self.__x = x
            self.__y = y

    def check_distance(self, other_point):
        return round(math.sqrt((self.__x - other_point.__x) ** 2 + (self.__y - other_point.__y) ** 2), 0)

    @property
    def point(self):
        return [self.__x, self.__y]

    @point.setter
    def point(self, values):
        x, y = values
        if self.check_coord(x, y):
            self.__x = x
            self.__y = y


#Инициализация объекта №1
p1 = Point(-4, 5)


#Инициализация объекта №2
p2 = Point(1, -2)


#Проверим координаты для p1 и p2
print("Координаты первой точки: ", p1.point)
print("Координаты второй точки: ", p2.point)


#Определим расстояние между координатами
print(p1.check_distance(p2))


#Изменим координаты объектов
p1.point = [-6, 0]
p2.point = [4, 8]
print("Координаты первой точки: ", p1.point)
print("Координаты второй точки: ", p2.point)


#Определим новое расстояние между координатами
print(p2.check_distance(p1))





