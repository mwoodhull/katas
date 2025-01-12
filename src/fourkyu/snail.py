import copy


def snail(snail_map):

    decoded_map = []

    snail_map_copy = copy.deepcopy(snail_map)

    while snail_map_copy:
        decoded_map.extend(snail_map_copy.pop(0))

        if snail_map_copy and snail_map_copy[0]:
            for lst in snail_map_copy:
                decoded_map.append(lst.pop())

        if snail_map_copy:
            decoded_map.extend(snail_map_copy.pop()[::-1])

        if snail_map_copy and snail_map_copy[0]:
            for lst in snail_map_copy[::-1]:
                decoded_map.append(lst.pop(0))

    return decoded_map
