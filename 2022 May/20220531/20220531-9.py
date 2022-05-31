#定義一個類描述平面上的點並提供移動點和計算到另一個點距離的方法

from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """
        初始化方法
        
        :param x: 橫坐標
        :param y: 縱坐標
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移動到指定位置
        
        :param x: 新的橫坐標
        "param y: 新的縱坐標
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移動指定的增量
        
        :param dx: 橫坐標的增量
        "param dy: 縱坐標的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        計算與另一個點的距離
        
        :param other: 另一個點
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
#說明： 本章中的插圖來自於Grady Booch等著作的《面向對象分析與設計》一書，該書是講解面向對象編程的經典著作，有興趣的讀者可以購買和閱讀這本書來了解更多的面向對象的相關知識。