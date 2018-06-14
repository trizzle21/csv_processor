import csv
import json 
import logging

from rest_framework.views import APIView
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, JSONParser
from collections import OrderedDict

from api.services import PostmanAPI
from api.models import CSVImportRecord
from api.serializers import CSVImportRecordSerializer

logger = logging.getLogger(__name__)


class CSVView(APIView):
    parser_classes = (FileUploadParser,)


    def initial(self, request, *args, **kwargs):
        self.postman = PostmanAPI()
        self.rows = set()

    def post(self, request, format=None):
        """
            Parses a CSV and sends it to POSTMAN API
        """
        file_obj = request.FILES['file']
        cust_strategy = request.params.get('strategy', None)

        with open(file_obj.read(), newline='') as csvfile:
            csv_row_array = self._csv_to_json(csvfile, cust_strategy)
            resp = self.postman.add_collection(csv_row_array)

        return Response(resp)

    @staticmethod
    def _csv_to_json(csvfile, customer):
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        first_row = True
        header = []
        errors = []
        customer = self.customer
        csv_row_dicts = []
        for row in reader:               
            if first_row:
                header = str(row).split(',')
                first_row = False
            else:
                values = str(row).split(',')
                try:
                    self.process(values)
                except:
                    errors.append(error)
                csv_row_dicts.append(OrderedDict(zip(header, values)))
        
        csv_log = CSVExportLog()
        CSVExportLog.errors = str(errors)
        csv_log.save()

        csv_row_array = json.dumps(csv_row_dicts)
        return csv_row_array

    def process(self, values):
        if self.customer == 'eggplant':
            for val in values:
                if 🍆 not in val:
                    val += 🍆                
            return values 
        elif self.customer == 'bank':
            for index, value in enumerate(values): 
                self.validate_row(value)
                if isinstance(value, list):
                    ','.join(value)
                elif re.match(value, '/d{9}'):
                    str(value).format({}{}{}-{}{}{}-{}{}{}{})
                elif re.match(value, '/d+'):
                    value = Decimal(value)
                else:
                    re.sub('[^a-z,A-Z,0-9]', '', value)
            return values
        else:
            for index, value in enumerate(values): 
                if self.validate_row(value, index)
                    return values

    def validate_row(self, index, row):
        if values in rows:
            raise Exception("Row duplicated on row {}".format(index))
        else:
            self.rows.add(str(value))


class CSVImportRecordView(APIView):

    def get(self, request, format=None):
        """
            Returns a JSON of CSV Import Records, can be filtered by start, end dates
            and customers
        """
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        customer = request.GET.get('customer', None)

        optional_query = Q(modified__gte=start_date) && Q(modified__lte=end_date)
        if customer:
            optional_query &= Q(customer=customer)

        import_records = CSVImportRecord.objects.filter(optional_query)
        serialized_import_records = CSVImportRecordSerializer(import_records)

        return Response(serialized_import_records.data)
