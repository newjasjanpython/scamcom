from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CodeSet

# Create your views here.


class IndexView(ListView):
    template_name = "list_codesets.html"
    model = CodeSet
    context_object_name = 'codesets'
    queryset = CodeSet.objects.all()

#    def get_queryset(self):
#        return super().get_queryset()


class CodeSetDetailView(DetailView):
    template_name = "detail_codeset.html"
    model = CodeSet
    context_object_name = 'codeset' # object -> codeset [Yani contextdagi obyekt o'zgaruvchi nomi]
    pk_url_kwarg = 'guid' # <uuid:guid> -> url ichidagi parametr nomi

