from django.shortcuts import render
from itertools import permutations
from ntpath import join
from PyDictionary import PyDictionary
from googletrans import Translator
translator = Translator()
dictionary=PyDictionary()
# Create your views here.
def hello(request):
    return render(request,'index.html')
def calculate(request):
    letter_input = request.GET.get('name')
    perms = [''.join(p) for p in permutations(letter_input)]
    wordlist=[]
    for i in range(0,len(perms)):
        combine_word = "".join(perms[i]) 
        valid_word = bool(dictionary.meaning(combine_word))
        if(valid_word==True):
            print(combine_word," has meaning")
            translate_word=translator.translate(combine_word,src="en",dest="th")
            wordlist.append(''.join((combine_word,": ",translate_word.text)))
    return render(request,'index.html',{
        'letter_input':letter_input,
        'wordlist':wordlist
    })