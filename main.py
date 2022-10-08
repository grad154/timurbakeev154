def spin_words(sentence):
    lst2 = sentence.split()
    count = 0
    for i in lst2:
        if len(i)>4:
            res = ''.join(reversed(i))
            lst2[count] = res
            res = ''
        count += 1
    sentence = " ".join(lst2)
    return sentence

sentence = input('enter the string')
print(spin_words(sentence))
