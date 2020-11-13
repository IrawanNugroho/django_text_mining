from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from main import forms


class TextPreprocessing(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'preprocessing/preprocessing.html'
    form_class = forms.PreprocessingForm

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})