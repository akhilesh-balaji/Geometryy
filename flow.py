from geometryy import *
from rich import print
import re

coordinate_re = r"[\-0-9]+[\.0-9]*,[\-0-9]+[\.0-9]*"
number_form_exception = "Input must be of the form x,y " \
    "where x and y are numbers. No whitespace around the comma"


def reflection():
    global number_form_exception

    a_str = input("Point A  = ")
    x_y_1 = re.match(coordinate_re, a_str)
    if not x_y_1:
        raise Exception(number_form_exception)
    a_xy = a_str.split(",")
    a = Coordinate(float(a_xy[0]), float(a_xy[1]))

    b_str = input("Point A' = ")
    x_y_2 = re.match(coordinate_re, b_str)
    if not x_y_2:
        raise Exception(number_form_exception)
    b_xy = b_str.split(",")
    b = Coordinate(float(b_xy[0]), float(b_xy[1]))

    print(f"\nThe mirror line {mirror_line(a, b)}")
    return mirror_line(a, b)


def dilation():
    global number_form_exception

    a_str = input("Point A  = ")
    x_y_1 = re.match(coordinate_re, a_str)
    if not x_y_1:
        raise Exception(number_form_exception)
    a_xy = a_str.split(",")
    a = Coordinate(float(a_xy[0]), float(a_xy[1]))

    a_img_str = input("Point A' = ")
    x_y_2 = re.match(coordinate_re, a_img_str)
    if not x_y_2:
        raise Exception(number_form_exception)
    a_img_xy = a_img_str.split(",")
    a_img = Coordinate(float(a_img_xy[0]), float(a_img_xy[1]))

    b_str = input("Point B  = ")
    x_y_3 = re.match(coordinate_re, a_str)
    if not x_y_3:
        raise Exception(number_form_exception)
    b_xy = b_str.split(",")
    b = Coordinate(float(b_xy[0]), float(b_xy[1]))

    b_img_str = input("Point B' = ")
    x_y_4 = re.match(coordinate_re, a_img_str)
    if not x_y_4:
        raise Exception(number_form_exception)
    b_img_xy = b_img_str.split(",")
    b_img = Coordinate(float(b_img_xy[0]), float(b_img_xy[1]))

    print(
        "\nThe scale factor [blue]k[/] = "
        f"{point_scale_enlargement(a, b, a_img, b_img)[0]}")
    print(
        "The centre of dilation [blue]C[/] = "
        f"{point_scale_enlargement(a, b, a_img, b_img)[1]}")
    return point_scale_enlargement(a, b, a_img, b_img)


def rotation():
    global number_form_exception

    a_str = input("Point A  = ")
    x_y_1 = re.match(coordinate_re, a_str)
    if not x_y_1:
        raise Exception(number_form_exception)
    a_xy = a_str.split(",")
    a = Coordinate(float(a_xy[0]), float(a_xy[1]))

    a_img_str = input("Point A' = ")
    x_y_2 = re.match(coordinate_re, a_img_str)
    if not x_y_2:
        raise Exception(number_form_exception)
    a_img_xy = a_img_str.split(",")
    a_img = Coordinate(float(a_img_xy[0]), float(a_img_xy[1]))

    b_str = input("Point B  = ")
    x_y_3 = re.match(coordinate_re, a_str)
    if not x_y_3:
        raise Exception(number_form_exception)
    b_xy = b_str.split(",")
    b = Coordinate(float(b_xy[0]), float(b_xy[1]))

    b_img_str = input("Point B' = ")
    x_y_4 = re.match(coordinate_re, a_img_str)
    if not x_y_4:
        raise Exception(number_form_exception)
    b_img_xy = b_img_str.split(",")
    b_img = Coordinate(float(b_img_xy[0]), float(b_img_xy[1]))

    print(
        "\nThe point of rotation [blue]P[/] = "
        f"{point_angle_rotation(a, b, a_img, b_img)[0]}")
    print(
        "The angle of rotation [blue]θ[/] ≈ "
        f"{point_angle_rotation(a, b, a_img, b_img)[1]}°")
    return point_angle_rotation(a, b, a_img, b_img)


def translation():
    global number_form_exception

    a_str = input("Point A  = ")
    x_y_1 = re.match(coordinate_re, a_str)
    if not x_y_1:
        raise Exception(number_form_exception)
    a_xy = a_str.split(",")
    a = Coordinate(float(a_xy[0]), float(a_xy[1]))

    b_str = input("Point A' = ")
    x_y_2 = re.match(coordinate_re, b_str)
    if not x_y_2:
        raise Exception(number_form_exception)
    b_xy = b_str.split(",")
    b = Coordinate(float(b_xy[0]), float(b_xy[1]))

    vector_formatted = str(
        translation_vector(
            a, b)).replace(
        "\n", "\n" + (" " * 28)).replace(".]", "]")

    print(f"\nThe translation vector [blue]T₁[/] = {vector_formatted}")
    return translation_vector(a, b)


logo_banner = \
    """[bold #D670D6]
  ______
 / _____)                       _
| /  ___  ____ ___  ____   ____| |_   ____ _   _[#6F3A6F] _   _[/]
| | (___)/ _  ) _ \\|    \\ / _  )  _) / ___) | | |[#6F3A6F] | | |[/]
| \\____/( (/ / |_| | | | ( (/ /| |__| |   | |_| |[#6F3A6F] |_| |[/]
 \\_____/ \\____)___/|_|_|_|\\____)\\___)_|    \\__  |[#6F3A6F]\\__  |[/]
                                          (____/[#6F3A6F](____/ [/][/] """ \
    """     By ([#21A2FF]αкнιℓєѕн[/], [#9BF00B]вαℓαᴊι[/])"""

print(f"{logo_banner}")
print("[blue][A][/] Reflection [#9BF00B](βeta)[/]\n"
      "[red][B][/] Dilation [#FFC225](αlpha)[/]\n"
      "[green][C][/] Rotation [#FFC225](αlpha)[/]\n"
      "[dim][yellow][D][/] Stretch[/dim]\n"
      "[cyan][E][/] Translation\n")

# [#FFC225](αlpha)[/]
# [#9BF00B](βeta)[/]


while True:
    transformation = str(input("Which transformation are you dealing with? "))

    options = ["A", "B", "C", "D", "E"]

    if transformation not in options:
        print("\nThe option specified is not in this list\n")
        continue
    else:
        break

if transformation == "A":
    reflection()
elif transformation == "B":
    dilation()
elif transformation == "C":
    rotation()
elif transformation == "D":
    print("[yellow]Coming[/] [dark_orange]Soon[/][yellow]![/]")
elif transformation == "E":
    translation()
