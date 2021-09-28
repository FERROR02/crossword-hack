from itertools import permutations
from ntpath import join
from PyDictionary import PyDictionary
dictionary=PyDictionary()
letter_input=str(input("ใส่ตัวอักษรที่ต้องการ: "))
perms = [''.join(p) for p in permutations(letter_input)]
print(perms)
word_list=[]
for i in range(0,len(perms)):
    combine_word = "".join(perms[i])
    valid_word = bool(dictionary.meaning(combine_word))
    if(valid_word==True):
        print(combine_word," has meaning")
        word_list.append(combine_word)
print(word_list)


letter_input = 'act'
    perms = [''.join(p) for p in permutations(letter_input)]
    print(perms)
    wordlist=[]
    for i in range(0,len(perms)):
        combine_word = "".join(perms[i])
        valid_word = bool(dictionary.meaning(combine_word))
        if(valid_word==True):
            print(combine_word," has meaning")
            wordlist.append(combine_word)