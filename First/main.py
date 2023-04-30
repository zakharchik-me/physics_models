import graphics as g
import time
import keyboard
from math import sqrt

x, y = 250, 1
speed_x= input('Set a speed on X \n')
speed_y =input('Set a speed on У\n ')
m = input('Ente weight of ball\n')
# speed_x, speed_y = 0, 0


SIZE_X = 500
SIZE_Y = 500

window = g.GraphWin("First", SIZE_X, SIZE_Y)

coord = g.Point(x, y)
velocity = g.Point(speed_x, speed_y)
tyga = g.Point(0, 0.98)
t = 0


# координаты тела
def add(point_1, point_2):
    new_point = g.Point(point_1.x + point_2.x,
                        round(point_1.y - point_2.y))

    return new_point


# создание тела
def draw_ball(coord):
    telo = g.Circle(coord, 10)
    telo.setFill('blue')
    telo.draw(window)


# чистка окна после завершения
def clear_window():
    rectangle = g.Rectangle(g.Point(0, 0), g.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('white')
    rectangle.draw(window)


# проверка координат для фбсолютно упргого сопротивления
def check_coord(coord, velocity, cos=228, sin=228):
    if cos == 228 and sin == 228:
        if coord.y < 0 or coord.y > SIZE_Y:
            velocity.y = - velocity.y
        if coord.x < 0 or coord.x > SIZE_X:
            velocity.x = - velocity.x
        if coord.y == SIZE_Y:
            velocity.y = - velocity.y // 2
    else:
        if coord.y < 0 or coord.y > SIZE_Y:
            velocity.y = -(velocity.y * sin) - 9.8
        if coord.x < 0 or coord.x > SIZE_X:
            velocity.x = -velocity.x
            # clear_window()
        if coord.y == SIZE_Y:
            velocity.y = (-velocity.y // 2)


#         if coord.x == SIZE_X or coord.x == 0:
#             clear_window()


# Tyga coord
def coord2(coord, velocity):
    return add(coord, velocity)


# F тяг
def velocity2(velocity, tyga):
    return add(velocity, tyga)


def find_vector_sin_cos(last_coords, current_coords):
    v_x = g.Point(current_coords.x - last_coords.x, 0)
    vector_coords = g.Point(current_coords.x - last_coords.x, current_coords.y - last_coords.y)
    cos = ((v_x.x * vector_coords.x) + (v_x.y * vector_coords.y)) / (
                sqrt((v_x.x ** 2) + (v_x.y ** 2)) * sqrt((vector_coords.x ** 2) + (vector_coords.y ** 2)))
    sin = 1 - (cos ** 2)
    return cos, sin


# живность процессу(фпс) - еудщ проги
while True:

    #     clear_window()
    draw_ball(coord)

    if t == 0:
        last_coordinates = coord
        coord = coord2(coord, velocity)
        velocity = velocity2(velocity, tyga)
        check_coord(coord, velocity)
    else:
        cos, sin = find_vector_sin_cos(last_coordinates, coord)
        last_coordinates = coord
        coord = coord2(coord, velocity)
        velocity = velocity2(velocity, tyga)
        check_coord(coord, velocity, cos=cos, sin=sin)

    t += 1

    g.time.sleep(0.1)
