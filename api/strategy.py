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
        return values

    def validate_row(self, value, index):
        if values['unique_id'].strip() in self.rows:
            raise StrategyException("Row duplicated on row {}".format(index))
        else:
            self.rows.add(str(values['unique_id']))


class DefaultStrategy(ProcessorStrategy):

    def __init__(self):
        self.rows = set()

    def process(self, values):
        for index, value in enumerate(values): 
            if self.validate_row(value)
                return values

    def validate_row(self, value, index):
        if values in self.rows:
            raise StrategyException("Row duplicated on row {}".format(index))
        else:
            self.rows.add(str(value))

class StrategyException(Exception):
    pass
