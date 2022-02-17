"""Services module."""

from fuzzywuzzy import process

class ExtractData:
    def __init__(self, options):
        self.options = options

    def extract_ratio_from_list(self, value):
        ratios = process.extract(value, self.options)
        highest = process.extractOne(value, self.options)
        return ratios, highest

class MatchingValuesService:

    def __init__(self, values, options):
        self.values = self.unique_values(values)
        self.options = self.unique_values(options)
        self.data_extractor = ExtractData(options)
        self.extracted_data = []
        self.extracted_data_with_ratios = []
    

    def get_each_value(self):
        for value in self.values:

            ratios, highest = self.data_extractor.extract_ratio_from_list(value)

            self.extracted_data.append((value, highest[0]))
            self.extracted_data_with_ratios.append((value, ratios))

        return self.extracted_data, self.extracted_data_with_ratios
    
    def unique_values(self, values):
        return list(set(values))

