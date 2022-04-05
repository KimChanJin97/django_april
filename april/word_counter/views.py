from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def result(request):
    sentence = str(request.POST.get("sentence")) # 안녕 안녕 안녕하세요
    sentence_to_list = sentence.split() # ["안녕", "안녕", "안녕하세요"]
    
    dictionary={}
    # EX) {단어1:개수1, 단어2:개수2 ...}
    
    for word in sentence_to_list:
        if word in dictionary:
            dictionary[word]+=1
        else:
            dictionary[word]=1
            
    #[(안녕,2), (안녕하세요,1)]
    word_count=list(dictionary.items())
    
    return render(request, 'result.html', {'word_count':word_count})
