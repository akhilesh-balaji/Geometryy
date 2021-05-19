#!/usr/bin/env python3
import numpy
import math


class Coordinate(object):
    """
    A Coordinate is of the form `(x,y)`

    Here, `x` represents the `x` coordinate
    while `y` represents the `y` coorinate on
    the Cartesian's plane.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return '(' + str(self.getX()) + ',' + str(self.getY()) + ')'

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __repr__(self):
        return "Coordinate(%d, %d)" % (self.x, self.y)


def midpoint(point1: Coordinate, point2: Coordinate) -> Coordinate:
    """Returns the midpoint of two coordinates specified."""

    a = point1
    b = point2
    midpoint_ab = Coordinate(
        (a.getX() + b.getX()) / 2,
        (a.getY() + b.getY()) / 2)
    return midpoint_ab


def perpendicular_bisector(
        point1: Coordinate,
        point2: Coordinate,
        standard_form: bool = False,
        lst_mb: bool = False):
    """
    Finds the perpendicular bisector of the segment
    connecting two points specified.
    """

    a = point1
    b = point2
    midpoint_ab = midpoint(a, b)
    try:
        slope_ab = (a.getY() - b.getY()) / (a.getX() - b.getX())
    except ZeroDivisionError:
        slope_ab = "%NaN%"

    if slope_ab != 0 and slope_ab != "%NaN%":
        slope_perp = float(-1 / slope_ab)

        if float(midpoint_ab.getY()) > 0:
            equation_perp = f"y = {slope_perp}x + " \
                f"{(-1*slope_perp*midpoint_ab.getX())+midpoint_ab.getY()}"
            equation_perp_std = f"-{slope_perp}x + y = " \
                f"{(-1*slope_perp*midpoint_ab.getX())+midpoint_ab.getY()}"
            b = (-1 * slope_perp * midpoint_ab.getX()) + midpoint_ab.getY()

        elif float(midpoint_ab.getY()) < 0:
            equation_perp = f"y = {slope_perp}x + " \
                f"{(-1*slope_perp*midpoint_ab.getX())-midpoint_ab.getY()}"
            equation_perp_std = f"-{slope_perp}x + y = " \
                f"{(-1*slope_perp*midpoint_ab.getX())-midpoint_ab.getY()}"
            b = (-1 * slope_perp * midpoint_ab.getX()) - midpoint_ab.getY()

        elif float(midpoint_ab.getY()) == 0:
            equation_perp = f"y = {slope_perp}x + " \
                f"{-1*slope_perp*midpoint_ab.getX()}"
            equation_perp_std = f"-{slope_perp}x + y = " \
                f"{(-1*slope_perp*midpoint_ab.getX())}"
            b = (-1 * slope_perp * midpoint_ab.getX())

    elif slope_ab == 0:
        slope_perp = "%NaN%"
        equation_perp = f"x = {midpoint_ab.getX()}"
        equation_perp_std = f"x + 0y = {midpoint_ab.getX()}"
        b = midpoint_ab.getX()

    elif slope_ab == "%NaN%":
        slope_perp = 0
        equation_perp = f"y = {midpoint_ab.getY()}"
        equation_perp_std = f"0x + y = {midpoint_ab}"
        b = midpoint_ab.getY()

    if standard_form is True:
        if lst_mb is True:
            return [equation_perp_std, [slope_perp, b]]
    else:
        if lst_mb is True:
            return [equation_perp, [slope_perp, b]]
        else:
            return equation_perp


def mirror_line(point1: Coordinate, point1_img: Coordinate):
    """
    Returns the mirror line of two points assuming that
    `a` has been reflected across an unknown line to
    create the image `a_img`.
    """

    a = point1
    a_img = point1_img
    return perpendicular_bisector(a, a_img)


def point_angle_rotation(
        point1: Coordinate,
        point2: Coordinate,
        point1_img: Coordinate,
        point2_img: Coordinate):
    """
    Returns the point of rotation and the angle of
    rotation given 2 object points, and their corresponding image points
    """

    a = point1
    b = point2
    a_img = point1_img
    b_img = point2_img
    perp_a_a_img_lst = perpendicular_bisector(
        a, a_img, standard_form=True, lst_mb=True)
    perp_b_b_img_lst = perpendicular_bisector(
        b, b_img, standard_form=True, lst_mb=True)
    perp_a_a_img = perp_a_a_img_lst[0]
    perp_b_b_img = perp_b_b_img_lst[0]

    if perp_a_a_img == "x = 0.0" and perp_b_b_img == "x = 0.0":
        # TODO: por is poi of equation of AB and A'B'
        por = Coordinate(0, 0)
    else:
        if (perp_a_a_img_lst[1][0]
                != "%NaN%" and perp_b_b_img_lst[1][0] != "%NaN%"):
            # When  perp_a_a_img_lst[1][0] == 0 and
            # perp_b_b_img_lst[1][0] == 0 por is poi
            # of equation of AB and A'B'
            # TODO

            # if perp_a_a_img_lst[1][0] == 0 and perp_b_b_img_lst[1][0] == 0:
            #     por = Coordinate(0.0, midpoint(a, a_img).getY())

            # else:
            lhs = numpy.array([[-perp_a_a_img_lst[1][0], 1], [
                -perp_b_b_img_lst[1][0], 1]])
            rhs = numpy.array([perp_a_a_img_lst[
                1][1], perp_b_b_img_lst[1][1]])
            por = Coordinate(
                numpy.linalg.solve(
                    lhs, rhs)[0], numpy.linalg.solve(
                    lhs, rhs)[1])

        elif (perp_a_a_img_lst[1][0] == "%NaN%"
              and perp_b_b_img_lst[1][0] != "%NaN%"):
            lhs = numpy.array([[1, 0], [
                -perp_b_b_img_lst[1][0], 1]])
            rhs = numpy.array([perp_a_a_img_lst[
                1][1], perp_b_b_img_lst[1][1]])
            por = Coordinate(
                numpy.linalg.solve(
                    lhs, rhs)[0], numpy.linalg.solve(
                    lhs, rhs)[1])

        elif (perp_a_a_img_lst[1][0] != "%NaN%"
              and perp_b_b_img_lst[1][0] == "%NaN%"):
            lhs = numpy.array([[-perp_a_a_img_lst[1][0], 1], [
                1, 0]])
            rhs = numpy.array([perp_a_a_img_lst[
                1][1], perp_b_b_img_lst[1][1]])
            por = Coordinate(
                numpy.linalg.solve(
                    lhs, rhs)[0], numpy.linalg.solve(
                    lhs, rhs)[1])

        elif (perp_a_a_img_lst[1][0] == "%NaN%"
              and perp_b_b_img_lst[1][0] == "%NaN%"):
            por = Coordinate(midpoint(a, a_img).getX(), 0.0)

    slope_a_por = (a.getY() - por.getY()) / (a.getX() - por.getX())
    slope_a_img_por = (a_img.getY() - por.getY()) / (a_img.getX() - por.getX())

    theta_rad = math.atan(
        (slope_a_por - slope_a_img_por)
        / (1 + (slope_a_por * slope_a_img_por)))
    theta_degrees = round(57.2958 * theta_rad, 3)
    return [por, theta_degrees]


def translation_vector(point1: Coordinate, point1_img: Coordinate):
    a = point1
    a_img = point1_img
    vector_x = float(a_img.getX() - a.getX())
    vector_y = float(a_img.getY() - a.getY())
    vector = numpy.array([[vector_x, vector_y]]).T

    return vector


def distance(point1: Coordinate, point2: Coordinate):
    a = point1
    b = point2
    distance = math.sqrt((b.getY() - a.getY()) ** 2
                         + (b.getX() - a.getX()) ** 2)
    return distance


def point_scale_enlargement(
        point1: Coordinate,
        point2: Coordinate,
        point1_img: Coordinate,
        point2_img: Coordinate):

    a = point1
    a_img = point1_img
    b = point2
    b_img = point2_img

    # try:
    #     k = a_img.getX() / a.getX()
    # except ZeroDivisionError:
    #     k = a_img.getY() / a.getY()

    k = distance(a_img, b_img) / distance(a, b)

    slope_a_a_img = (a_img.getY() - a.getY()) / (a_img.getX() - a.getX())
    slope_b_b_img = (b_img.getY() - b.getY()) / (b_img.getX() - b.getX())

    if a.getY() < 0:
        b_a = (-1 * slope_a_a_img * a.getX()) - a.getY()
    elif a.getY() > 0:
        b_a = (-1 * slope_a_a_img * a.getX()) + a.getY()
    elif a.getY() == 0:
        b_a = -1 * slope_a_a_img * a.getX()

    if b.getY() < 0:
        b_b = (-1 * slope_b_b_img * b.getX()) - b.getY()
    elif b.getY() > 0:
        b_b = (-1 * slope_b_b_img * b.getX()) + b.getY()
    elif b.getY() == 0:
        b_b = -1 * slope_b_b_img * b.getX()

    lhs = numpy.array([[-slope_a_a_img, 1], [
        -slope_b_b_img, 1]])
    rhs = numpy.array([b_a, b_b])
    coe = Coordinate(
        numpy.linalg.solve(
            lhs, rhs)[0], numpy.linalg.solve(
            lhs, rhs)[1])

    return [k, coe]


# -------------------------
#  ******  Tests  ******
# -------------------------

# # Mirror Line Test
# c1 = Coordinate(-4, 4)
# c2 = Coordinate(-4, 2)
# print(c1)
# print(c2)

# print(mirror_line(c1, c2))

# # PoR & Angle Test
# a = Coordinate(1, 1)
# b = Coordinate(2, 2)
# a_img = Coordinate(-1, 1)
# b_img = Coordinate(-2, 2)

# print(point_angle_rotation(a, b, a_img, b_img))

# # Translation test
# a = Coordinate(1, 2)
# # [4,-3] -> vector
# a_img = Coordinate(5, -1)

# print(translation_vector(a, a_img))

# Dilation test
# a = Coordinate(5, 6)
# b = Coordinate(6, 8)
# a_img = Coordinate(35, 42)
# b_img = Coordinate(540, 720)

# a = Coordinate(1, 2)
# b = Coordinate(3, 3)
# a_img = Coordinate(0, 3)
# b_img = Coordinate(4, 5)

# print(point_scale_enlargement(a, b, a_img, b_img))
