from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from main import forms
from utils.TextPreprocessing import tokenization, stemming, lemmatization, stop_words
from django.http import JsonResponse
import json



class TextPreprocessing(View):
    template_name = 'preprocessing/preprocessing.html'
    form_class = forms.PreprocessingForm

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # return HttpResponse(json.loads(request.POST['json_data'])['message'])
        result = tokenization(json.loads(request.POST['json_data'])['message'])
        result = stemming(result)
        result = lemmatization(result)
        result = stop_words(result)
        # return JsonResponse(result, safe=False)
        return HttpResponse(result)