# from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from main import forms
from utils.TextPreprocessing import tokenization, stemming, lemmatization, stop_words
from django.http import JsonResponse



class TextPreprocessing(View):
    template_name = 'preprocessing/preprocessing.html'
    form_class = forms.PreprocessingForm

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        result = tokenization(request.POST['message'])
        result = stemming(result)
        result = lemmatization(result)
        result = stop_words(result)
        return JsonResponse(result, safe=False)