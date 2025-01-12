def snail(snail_map):

    if len(snail_map) < 3:
        for i in snail_map:
            if i == snail_map[0]:
                decoded_map = snail_map[0]
        
            elif i == snail_map[-1]:
                for num in i[::-1]:
                    decoded_map.append(num)

        return decoded_map

    if len(snail_map) == 3:

        for i in snail_map:
            if i == snail_map[0]:
                decoded_map = snail_map[0]
            
            elif i == snail_map[-1]:
                for num in i[::-1]:
                    decoded_map.append(num)

                for lst in snail_map[1][:-1]:
                    decoded_map.append(lst)

            else:
                decoded_map.append(i[-1])
        
        return decoded_map

    if len(snail_map) > 3:

        for i in snail_map:
            if i == snail_map[0]:
                decoded_map = snail_map[0]
            
            elif i == snail_map[-1]:
                for num in i[::-1]:
                    decoded_map.append(num)
                    

                for lst in snail_map[::-1]:
                    if lst[0] not in decoded_map:
                        decoded_map.append(lst[0])
                    else:
                        for num in lst:
                            decoded_map.append(num)
                    
                decoded_map.pop()

            else:
                decoded_map.append(i[-1])
        
        return decoded_map