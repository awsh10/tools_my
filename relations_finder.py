import pickle
from time import time
import os
import glob

horizontal, vertical, points_tuple_set = [], [], set()
calls = 0

def bord_create_func(board_size=10000):
    """
    Creates full board with board_size ** 2 elements
    :param board_size: size of board
    :param elements_max: max quantity of elements in a subboard
    :return:
    """
    global horizontal

    vertical = [str(v) for v in range(board_size - 1, -1 , -1)]
    horizontal = [str(h) for h in range(board_size)]
    board = [h + ':' + v for v in vertical for h in horizontal]

    return board

def fields_rest_func(field, fields_set):
    """ Creates new rest list of free fields for the given field.  Finds diagonal, vertical and horizontal fields
        binded with this field and subtracts them from the input board_rest_set """
    horizontal_value, sep, vertical_value   = field.partition(':')
    horizontal_point = int(horizontal_value)
    vertical_point = board_size - 1 - int(vertical_value)

    horizontal_left = horizontal[:horizontal_point]
    horizontal_right = horizontal[horizontal_point + 1:]
    vertical_down = vertical[vertical_point + 1:]
    vertical_up = vertical[:vertical_point]
    fields_vertical_list = [horizontal_value + ':' + v for v in vertical if v != vertical_value]
    fields_horizontal_list = [h + ':' + vertical_value for h in horizontal if h != horizontal_value]

    diagonal_left_down = list(h + ':' + v for (v, h) in zip(vertical_down, reversed(horizontal_left)))
    diagonal_rigt_down = list(h + ':' + v for (v, h) in zip(vertical_down, horizontal_right))
    diagonal_rigt_up = list(h + ':' + v for (v, h) in zip(reversed(vertical_up), horizontal_right))
    diagonal_left_up = list(h + ':' + v for (v, h) in zip(reversed(vertical_up), reversed(horizontal_left)))

    total_fields_list = (diagonal_rigt_down + diagonal_left_down + diagonal_rigt_up + diagonal_left_up +
                         fields_vertical_list + fields_horizontal_list + [field])
    fields_rest_set = fields_set.difference(set(total_fields_list))

    return fields_rest_set

def point_func(fields_set, points_list=[], level=0):
    """
    This recursive function finds variants of lacations points on the board with given count of fields
    """

    global calls

    calls += 1
    # Recursion
    points_level_list = points_list
    # print('field_set: {}'.format(fields_set))
    for field in fields_set:
        points_list = points_level_list + [field]
        fields_rest_set = fields_rest_func(field, fields_set)
        len_set = len(fields_rest_set)
        if len_set <= 1:
            if len_set == 1:
                points_list.append(fields_rest_set.pop())
            points_list.sort()
            points_tuple_set.add(tuple(points_list))
            return
            # points_list_list.append(points_list)
            # points_list.append(list(fields_set)[0])
        else:
            # Recorsion
            point_func(fields_rest_set, points_list, level=level + 1)

    return

def main_func(board_size = 8, elements_max=None):

    start = time()
    board = bord_create_func(board_size)
    time_func_board = time() - start
    point_func(set(board), level=0)

    time_func_point = time() - time_func_board
    time_exec = time() - start
    time_creating_element = time_func_board / board_size / board_size
    print(sorted(list(points_tuple_set)))
    return {'time_func_board': '{:.3g}'.format(time_func_board),
            'time_creating_element': '{:.3g}'.format(time_creating_element),
            'time_func_point': '{:.3g}'.format(time_func_point),
            'time_exec': '{:.3g}'.format(time_exec)}


if __name__ == '__main__':
    from tools_my import convert_to_exponent_float
    board_size = 5
    elements_max = None
    d = main_func(board_size, elements_max)
    width = 30
    format_my = '{0:{1}}: {2}'
    print(format_my.format('time_func_board', width, convert_to_exponent_float(d['time_func_board'], digit=0)),
          format_my.format('time_creating_element', width, convert_to_exponent_float(d['time_creating_element'])),
          format_my.format('time_execution', width, d['time_exec']),
          sep='\n')
