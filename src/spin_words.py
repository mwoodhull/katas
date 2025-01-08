def spin_words(sentence):

    list_sentence = sentence.split()

    for i in range(len(list_sentence)):
        if len(list_sentence[i]) >= 5:
            list_sentence[i] = list_sentence[i][::-1]

    final_sentence = ' '.join(list_sentence)
    
    return final_sentence