def mexican_wave(people):
    
    wave = []
    queue = list(people)

    for i in range(len(queue)):

        mex_queue = queue[i].capitalize()
        print(mex_queue)
        wave.append(''.join(mex_queue))

    return wave