def mexican_wave(people):

    wave = []
    queue = list(people)

    if len(queue) == 0:
        return wave

    for i in range(len(queue)):

        if 122 >= ord(queue[i]) >= 97:
            queue[i] = queue[i].capitalize()
            wave.append("".join(queue))
            queue[i] = queue[i].lower()

    return wave
