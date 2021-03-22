def find_word(sentence, target_word):
    result = []
    sentence = sentence.replace("."," ").replace(","," ").split(" ")
    sentence = list(filter(None,sentence))

    for i, word in enumerate(sentence):
        if word.lower() == target_word.lower():
            result.append(i)
    return result
    
