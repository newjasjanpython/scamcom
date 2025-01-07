from django.urls import path
from .views import IndexView, CodeSetDetailView


app_name = 'main'


urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('codeset/<uuid:guid>/', CodeSetDetailView.as_view(), name='codeset_detail_page'),
]


