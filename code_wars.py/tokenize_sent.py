import string
def tokenized_sentence(sentence):
    sentence=sentence.split(' ')
    new_sentence = []
    for i in range(len(sentence)):
        if i == ',!()}{:;#@$%^*-_+=?><.':
            sentence.pop([i])
        else:
            new_sentence.append(sentence[i])

    new_sentence = sorted(new_sentence)
    new_list = []
    for i in range(len(new_sentence)):
        new_sentence.append([i])
    return new_sentence


    #sentence=sentence.split(' ')
    #for val in sentence:
    #    if val not in 'abcdefghijklmnopqrstuvwxyz':
    #        sentence = sentence.replace(val, '')
    #sentence=sentence.split(' ')
    #print(sentence)
    #sentence=sorted(sentence)
    #print(sentence)

tokenized_sentence('they know her , jill . but she does not know them .')