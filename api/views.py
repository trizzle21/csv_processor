import csv
import json
import logging

from rest_framework.views import APIView
from django.http import JsonResponse
from strategy import EggPlantStrategy, BankStrategy, DefaultStrategy, StrategyException

from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, JSONParser
from collections import OrderedDict

from api.services import PostmanAPI
from api.models import JSONImportLog, CSVImportLog

logger = logging.getLogger(__name__)

STRATEGIES = {
    'eggplant': EggPlantStrategy,
    'Bank of the USA': BankStrategy, 
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
        customer = request.POST.get('customer', None)

        with open(file_obj.read(), newline='') as csvfile:
            processed_list_from_csv = self._csv_to_json(csvfile, cust_strategy)
            resp = self.postman.add_collection(processed_dictionary_from_csv)

        return Response(resp)

    def _record_log_file(self, errors):
        csv_log = CSVExportLog()
        CSVImportLog.errors = str(errors)
        CSVImportLog.customer = self.customer_strategy
        csv_log.save()

    def _csv_to_json(self, csvfile, customer):
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        first_row = True
        header = []
        errors = []

        csv_row_dicts = []
        self.customer_strategy = STRATEGIES.get(customer, 'default')
        header = str(next(reader)).split(',')        
        for row in reader:               
            values = str(row).split(',')
            try:
                customer_strategy.process(values)
            except StrategyException as error:
                errors.append(error)
            imported_dict.append(OrderedDict(zip(header, values)))
        
        self._record_log_file(errors)

        json_of_csv_rows = json.dumps(csv_row_dicts)
        return json_of_csv_rows

class CSVImportRecordView(APIView):

    def get(self, request, format=None):
        """
            Parses a CSV and sends it to POSTMAN API
        """
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

        query_ = Q(modified__gte=start_date) && Q(modified__lte=end_date)
        #TODO
        import_records = CSVImportRecord.objects.filter(modified)

        return Response(resp)

