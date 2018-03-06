from django.urls import path
from api.views import CSVView, JSONView

urlpatterns = [
    path('csv', CSVView.as_view()),
    path('json', JSONView.as_view())

]
