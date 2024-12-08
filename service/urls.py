from django.urls import path
from .views import ServicesView, ServiceDetailsView


app_name = 'service'

urlpatterns = [
    path('', ServicesView.as_view(), name='page'),
    path('details/', ServiceDetailsView.as_view(), name='details'),
]