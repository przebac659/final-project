from yahoofinancials import YahooFinancials
import numpy as np
from sklearn.preprocessing import minmax_scale
from variables import Variables


class Data:

    def __init__(self, company_enum):
        # Variables
        self.company_name = Variables.company_name[company_enum]
        self.price_type = Variables.price_type

        # Time interval
        self.startDate = Variables.startDate
        self.endDate = Variables.endDate
        self.interval = Variables.interval

        # Shape of input data
        self.chunkSize = Variables.chunkSize

        # Initial arrays
        self.data_prediction = []
        self.data_result = []
        self.data = []

    def prepare_arrays(self):
        yahoo_financials = YahooFinancials(self.company_name)
        # balance_sheet_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')
        data_prices_raw = yahoo_financials.get_historical_price_data(self.startDate, self.endDate, self.interval)
        data_prices = data_prices_raw[self.company_name]['prices'] # access the inner dictionary as the raw data is in JSON
        print(data_prices)

        self.highest_price = 0
        for i in range(len(data_prices)):
          if (self.highest_price < data_prices[i][self.price_type]):
            self.highest_price = i

        for i in range(len(data_prices)):
          self.data.append(data_prices[i][self.price_type])

        for i in range(self.chunkSize, len(data_prices) - 1):
          self.data_prediction.append(self.data[i-self.chunkSize:i]) 
          self.data_result.append(self.data[i])

        return self.highest_price

    def reshape_data(self):
        self.data_result, self.data_prediction = np.array(self.data_result), np.array(self.data_prediction)

        self.data_prediction = minmax_scale(self.data_prediction, feature_range=(0,.999))
        self.data_prediction = np.reshape(self.data_prediction, (self.data_prediction.shape[0], self.data_prediction.shape[1], 1))
        self.data_result = minmax_scale(self.data_result, feature_range=(0,.999))

        return self.data_prediction, self.data_result
