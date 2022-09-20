import random as r
import turtle as t
"""Setup"""
screen_tur = t.Screen()
draw_tur = t.Turtle()
draw_tur.speed(4)

class Point:
    def __init__(self):
        self.x = r.randint(-100, 100)
        self.y = r.randint(-100, 100)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self):
        return "".join(["(", str(self.x), ",", str(self.y), ")"])

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)


class Line:

    def __init__(self,n):
        """Generate points for line"""
        self.point_list = []
        for i in range(n):
            x = Point()
            self.point_list.append(x)

    def get_x(self):
        x_list = [ele.get_x() for ele in self.point_list]
        return x_list

    def get_y(self):
        y_list = [ele.get_y() for ele in self.point_list]
        return y_list

    def __str__(self):
        """2.1"""
        str_point = ""
        for point in self.point_list:
            str_point += "(" + str(point.get_x()) + "," + str(point.get_y()) + "), "
        str_point = str_point[:-2]
        return str_point

    def join(self, other):
        """2.2"""
        times = len(other.point_list)
        for i in range(times):
            self.point_list.append(other.point_list[0])
            other.point_list.pop(0)

        return self.point_list

    def join_extend(self, other):
        """2.2 extend"""
        self.point_list.extend(other.point_list)
        other.point_list.clear()
        return self.point_list

    def zigzag1(self, other):
        """2.3"""
        line3 = []
        if len(self.point_list) > len(other.point_list):
            times = len(other.point_list)
            for i in range(1, times * 2, 2):
                point1 = self.point_list[0]
                self.point_list.pop(0)

                point2 = other.point_list[0]
                other.point_list.pop(0)

                line3.insert(i, point1)
                line3.insert(i, point2)

            for point in self.point_list:
                line3.insert(len(line3), point)

        else:

            times = len(self.point_list)
            for i in range(1, times * 2, 2):
                point1 = self.point_list[0]
                self.point_list.pop(0)

                point2 = other.point_list[0]
                other.point_list.pop(0)

                line3.insert(i, point1)
                line3.insert(i, point2)

            for point in other.point_list:
                line3.insert(len(line3), point)
                other.point_list.pop(0)

        return line3

    def zigzag2(self, other):

        """2.4"""
        times = len(other.point_list)

        for i in range(1, times*2, 2):

            point = other.point_list[0]
            other.point_list.pop(0)

            self.point_list.insert(i, point)

        return self.point_list


def draw_line(point_list, color):

    draw_tur.penup()
    draw_tur.color(color)
    count = 0

    for ele in point_list:
        count += 1
        draw_tur.goto(ele.get_x(), ele.get_y())
        draw_tur.pendown()
        draw_tur.dot(5, "blue")
        draw_tur.write(str(count) + "." + "(" + str(ele.get_x()) + ", " + str(ele.get_y()) + ")")

    draw_tur.penup()


def draw_result(point_list, color):

    draw_tur.penup()
    draw_tur.color(color)
    draw_tur.pensize(2)
    count = 0

    for ele in point_list:
        count += 1
        draw_tur.goto(ele.get_x(), ele.get_y())
        draw_tur.pendown()
        draw_tur.dot(5, "blue")
        draw_tur.penup()
        draw_tur.rt(90)
        draw_tur.forward(30)
        draw_tur.write(str(count), align="right", font=('Arial', 14, 'normal'))
        draw_tur.backward(30)
        draw_tur.lt(90)
        draw_tur.pendown()

    draw_tur.penup()

"""===================================================================="""

class LineTester:

    def __init__(self):
        self.check = True

    def join_check(self, line1, line2):

        draw_line(line1.point_list, "brown")
        draw_line(line2.point_list, "gray")

        # join_line = line1.join(line2)
        join_line = line1.join_extend(line2)
        draw_result(join_line, "blue")

        return self.check

    def zigzag_check(self, line1, line2):
        draw_line(line1.point_list, "pink")
        draw_line(line2.point_list, "gray")

        # zigzag_line = line1.zigzag1(line2)
        zigzag_line = line1.zigzag2(line2)
        draw_result(zigzag_line, "blue")

        return self.check

"""===================================================================="""
u=input("line 1:")
v=input("line 2:")

a = Line(int(u))
b = Line(int(v))
linetest = LineTester()

"""str"""
print(a.__str__())
print(b.__str__())

"""Test join"""
# result = linetest.join_check(a, b)

"""test zigzag"""
result = linetest.zigzag_check(a, b)

print("This is the result of checking: " + str(result))

t.exitonclick()