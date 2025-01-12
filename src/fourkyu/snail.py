import copy

def snail(snail_map):

    # if len(snail_map) < 3:
    #     for lst in snail_map:
    #         if lst == snail_map[0]:
    #             for num in snail_map[0]:
    #                 decoded_map.append(num)

    #         elif lst == snail_map[-1]:
    #             for num in lst[::-1]:
    #                 decoded_map.append(num)

    #     return decoded_map

    # if len(snail_map) == 3:

    #     for i in snail_map:
    #         if i == snail_map[0]:
    #             decoded_map = snail_map[0]
            
    #         elif i == snail_map[-1]:
    #             for num in i[::-1]:
    #                 decoded_map.append(num)

    #             for lst in snail_map[1][:-1]:
    #                 decoded_map.append(lst)

    #         else:
    #             decoded_map.append(i[-1])
        
    #     return decoded_map

    # if len(snail_map) > 3:
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


        # for i in snail_map:
        #     if i == snail_map[0]:
        #         decoded_map = snail_map[0]
        #         for lst in snail_map:
        #             decoded_map.append(snail_map[lst][-1])
            
        #     elif i == snail_map[-1]:
        #         for num in i[::-1]:
        #             decoded_map.append(num)
                    

        #         for lst in snail_map[::-1]:
        #             if lst[0] not in decoded_map:
        #                 decoded_map.append(lst[0])
        #             else:
        #                 for num in lst:
        #                     decoded_map.append(num)
                    
        #         decoded_map.pop()

        #     else:
        #         decoded_map.append(i[-1])
        
        # return decoded_map