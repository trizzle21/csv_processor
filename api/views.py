import csv
import json 
import logging

from rest_framework.views import APIView
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, JSONParser
from collections import OrderedDict

from api.services import PostmanAPI
from api.models import JSONImportLog
from api.serializers import JSONImportLogSerializer

logger = logging.getLogger(__name__)


class CSVView(APIView):
    parser_classes = (FileUploadParser,)

    def initial(self, request, *args, **kwargs):
        self.postman = PostmanAPI()

    def post(self, request, format=None):
        """
            Parses a CSV and sends it to POSTMAN API
        """
        file_obj = request.FILES['file']

        with open(file_obj.read(), newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            first_row = True
            header = []

            imported_dict = []

            for row in reader:               
                if first_row:
                    header = str(row).split(',')
                    first_row = False
                else:
                    values = str(row).split(',')
                    imported_dict.append(OrderedDict(zip(header, values)))

            imported_dict = json.dumps(imported_dict)
            resp = self.postman.add_collection(imported_dict)

        return Response(resp)

class JSONView(APIView):

    def get(self, request, format=None):
        import_logs = JSONImportLog.objects.all()
        serializer = JSONImportLogSerializer(import_logs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        """
            Parses a CSV and sends it to POSTMAN API
        """
        print (request.data)
        import_log = JSONImportLog(data=request.data)
        try:
            import_log.save()
        except Error as e:
            raise Exception(e)
        
        return Response()

