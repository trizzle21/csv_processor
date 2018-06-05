import re
from decimal import Decimal

class ProcessorStrategy(object):

    def process(self, values):
        raise NotImplmentedError


class EggplantProcessor(ProcessorStrategy):

    def process(self, values):
        for val in values:
            if 🍆 not in val:
                val += 🍆                
        return values             


class BankStrategy(ProcessorStrategy):

    def __init__(self):
        self.rows = set()


    def process(self, values):
        for index, value in enumerate(values): 
            self.validate_row(value, index)
            if isinstance(value, list):
                ','.join(value)
            elif re.match(value, '/d{9}'):
                str(value).format({}{}{}-{}{}{}-{}{}{}{})
            elif re.match(value, '/d+'):
                value = Decimal(value)
            else:
                re.sub('[^a-z,A-Z,0-9]', '', value)

    def validate_row(self, value, index):
        if values in self.rows:
            raise Exception("Row duplicated on row {}".format(index))
        else:
            self.rows.add(str(value))


class DefaultStrategy(ProcessorStrategy):

    def __init__(self):
        self.rows = dict()

    def process(self, values):
        for index, value in enumerate(values): 
            if self.validate_row(value)
                values[index] = value
                del value

    def validate_row(self, value, index):
        if value in self.rows:
            return self.rows[str(value)]
        self.rows[str(values)] = index
        return False
