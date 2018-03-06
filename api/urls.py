from django.urls import path
from api.views import CSVView

urlpatterns = [
    path('csv', CSVView.as_view())
]
