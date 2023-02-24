from django.shortcuts import render
from dictionary import words
from dictionary import dictionary
from django.contrib import messages
from dictionary import anagram_checker
from django.http import HttpResponse

def HomePage(request):
    return render(request, 'main/index.html')
def IndexPage(request):
    if request.method == "POST":
        try:
            #word subset view
            worda = (request.POST.get('word').lower()).strip()
            final_words = words.all_real_combinations(worda)
            scrabble_word_count = words.get_points(worda)
            context = {'final': final_words, 'words' : worda.capitalize(), 'count': len(final_words),
                    'scrabble_word_count': scrabble_word_count, 'len_word':len(worda),
                    }
            return render(request, "main/form-words.html", context)
        except:
            return HttpResponse('''
                                <div>How come you're seeing this🤨, You clearly didn't read the instructions, or maybe you're deliberately trying to mess with me</div><br>
                                <span>Well, here are the instructions again, in bold this time, you can't say you didn't see it this time</span><br>                            
                                <h1>Enter only alphabets of the english language, uppercase or lower case.</h1> 
                                <h1>Do not add phrases with punctuation marks, spaces or symbols.</h1>
                                <a href="http://127.0.0.1:8000">Go back and try again</a>
                                ''')
    return render(request, "main/form-words.html")

def DictionarySearch(request):
    if request.method == "POST":
        wordb = request.POST.get('word_search')
        result_of_search = dictionary.the_dictionary(wordb)
        synonym_check = dictionary.synonym_dictionary(wordb)
        anagram_check = anagram_checker.check_anagram(wordb)
        context = {'result':result_of_search, 'word':wordb.lower().strip(), 
                   "anagram":anagram_check, 'dictionary':dictionary.my_dictionary, 
                   'synonym':synonym_check, 'counti': 1,
                   }
        return render(request, "main/DictionarySearch.html", context)
    return render(request, "main/DictionarySearch.html")
