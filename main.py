import sys

import sortedcontainers


def find_outline_points(boxes):
    result = list()
    end_points = list()

    for box in boxes:
        # height for starting point is negative to process higher height start points before lower height start points for same x
        end_points.append((box[0], -box[2]))
        end_points.append((box[1], box[2]))
    end_points = sorted(end_points, key=lambda i: (i[0], i[1]))

    height_list = sortedcontainers.SortedList()
    height_list.add(0)

    for pt in end_points:
        x, ht = pt
        if ht < 0:  # start point
            if abs(ht) > height_list[-1]:  # current height is higher, so include in result
                result.append([x, abs(ht)])
            height_list.add(abs(ht))  # update max_height
        else:  # end point
            height_list.remove(ht)  # remove current height from list
            if ht > height_list[-1]:  # max_height is less than previous value (dip in structure), include in result
                result.append([x, height_list[-1]])
    return result


def main():
    input_list = [
        [(1, 5, 10), (4, 6, 8), (10, 15, 10), (11, 12, 8)],
        [(1, 10, 4), (1, 8, 6), (1, 6, 8)],
        [(0, 6, 2), (5, 10, 8), (7, 8, 12)],
    ]

    for count, curr_input in enumerate(input_list):
        result = find_outline_points(boxes=curr_input)
        print(f'{count + 1} : {result}')

    sys.exit(0)


if __name__ == '__main__':
    main()
