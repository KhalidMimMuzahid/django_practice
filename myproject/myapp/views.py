from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    return render(request, 'index.html')
def form(request):
    context={
        "name": "Khalid",
        "age": 36,
        "nationality": "Bangladeshi"
    }
    return render(request, 'form.html',context)
def counter(request):
    # words= request.GET['words'] # words is coming from query?words=   parameter  #for GET method
    words= request.POST['words'] # words is coming from csrf_token   #for POST method method
    wordsCount= len(words.split())
    return render(request, 'counter.html', {"words_count": wordsCount}  )