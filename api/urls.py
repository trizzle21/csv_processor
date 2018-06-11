from django.urls import path
from api.views import CSVView, CSVImportRecordView

urlpatterns = [
    path('csv/', CSVView.as_view()),
    path('csv-record-import/', CSVImportRecordView.as_view())
]
