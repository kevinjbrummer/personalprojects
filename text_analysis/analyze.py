import bokkochan

def count_words(text):
    words = text.split()
    end_char = '.,!?:;"()'
    for i in range(len(words)):
        if words[i][-1] in end_char:
            temp = ''
            for j in words[i]:
                if not j in end_char:
                    temp = temp + j
            words[i] = temp
    total_words = len(words)
    return total_words

def count_sentences(text):
    counter = 0
    terminals = '.?!;'
    for char in text:
        if char in terminals:
            counter = counter + 1
    return counter

def count_syllables(text):
    counter = 0
    words = text.split()
    for word in words:
        syllables = count_syllables_in_word(word)
        counter = counter + syllables
    return counter

def count_syllables_in_word(word):
    word = remove_punctuation(word)
    counter = 0
    vowel = 'aeiouAEIOU'
    prev_vowel = False
    if len(word) <= 3:
        return 1
    if word[-1] in 'Ee':
        word = word[0:-1]
    if word[-1] in 'Yy':
        counter = counter +1
    for char in word:
        if char in vowel:
            if not prev_vowel:
                counter = counter + 1
            prev_vowel = True
        else:
            prev_vowel = False
    return counter

def remove_punctuation(word):
    punctuation = '!“”"().,;:?'
    abbr = True
    number = '0123456789'
    vowel = 'AEIOUYaeiouy'
    for char in word:
        if char in number:
            return word
        if char in vowel:
            abbr = False
    if abbr:
        return word
    while word[-1] in punctuation:
        word = word[0:-1]
    while word[0] in punctuation:
        word = word[1:len(word)]
    return word

def output_results(score):
    if score >= 90.0:
        print('5th grade reading level.')
    elif score >= 80.0:
        print('6th grade reading level.')
    elif score >= 70.0:
        print('7th grade reading level.')
    elif score >= 60.0:
        print('8-9th grade reading level.')
    elif score >= 50.0:
        print('10-12th grade reading level.')
    elif score >= 30.0:
        print('College student reading level.')
    else:
        print('College graduate reading leve.')
    
def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    total_words = count_words(text)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(text)
    score = (206.835 - 1.015 * (total_words / total_sentences)
            - 84.6 * (total_syllables / total_words))

    output_results(score)


compute_readability(bokkochan.text)
