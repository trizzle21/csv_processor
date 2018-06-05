import csv
import json 
import logging

from rest_framework.views import APIView
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, JSONParser
from collections import OrderedDict

from api.services import PostmanAPI
from api.models import JSONImportLog, CSVExportLog
from api.serializers import JSONImportLogSerializer

logger = logging.getLogger(__name__)

STRATEGIES = {
    'eggplant': EggPlantStrategy,
    'Bank of the USA': BankStrategy, 
    'whompa': None, 
    'default': DefaultStrategy
}


class CSVView(APIView):
    parser_classes = (FileUploadParser,)


    def initial(self, request, *args, **kwargs):
        self.postman = PostmanAPI()

    def post(self, request, format=None):
        """
            Parses a CSV and sends it to POSTMAN API
        """
        file_obj = request.FILES['file']
        cust_strategy = request.params.get('strategy', None)

        with open(file_obj.read(), newline='') as csvfile:
            imported_dict = self._csv_to_json(csvfile, cust_strategy)
            resp = self.postman.add_collection(imported_dict)

        return Response(resp)

    @staticmethod
    def _csv_to_json(csvfile, customer):
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        first_row = True
        header = []
        errors = []

        imported_dict = []
        strategy = STRATEGIES.get(customer, 'default')
        for row in reader:               
            if first_row:
                header = str(row).split(',')
                first_row = False
            else:
                values = str(row).split(',')
                try:
                    strategy.process(values)
                except:
                    JSONImportLogSerializer
                imported_dict.append(OrderedDict(zip(header, values)))
        
        csv_log = CSVExportLog()
        CSVExportLog.errors = str(errors)
        csv_log.save()
        
        imported_dict = json.dumps(imported_dict)
        return imported_dict


class JSONView(APIView):

    def get(self, request, format=None):
        import_logs = JSONImportLog.objects.all()
        serializer = JSONImportLogSerializer(import_logs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        """
            Parses a CSV and sends it to POSTMAN API
        """
        import_log = JSONImportLog(data=request.data)
        try:
            import_log.save()
        except Error as e:
            raise Exception(e)
        
        return Response()


