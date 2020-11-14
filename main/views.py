from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from main import forms


class TextPreprocessing(View):
    template_name = 'preprocessing/preprocessing.html'
    form_class = forms.PreprocessingForm

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return HttpResponse(request.POST['message'])