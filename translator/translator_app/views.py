from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from googletrans import Translator
# Create your views here.

def index(request):
    translation = None
    if request.method == "POST":
        text = request.POST.get("translate")
        language = request.POST.get("language")
        translator = Translator()
        translation = translator.translate(text, dest=language).text
    return render(request, "home.html", {"translation": translation})
