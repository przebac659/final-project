# Projekt inżynierski
# Final project

# Stock price prediction

# author: Baca Przemysław
# tutor: dr Anna Gorawska

import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication
from sys import argv
from data_handler import Data
from neural_network import NeuralNetwork
from graphics import MainWindow
from variables import Variables
from sklearn.preprocessing import minmax_scale

company_enum = 0

def print_results(future_price, data_result, highest_price):
    # print(data_result)
    data_result = minmax_scale(data_result, feature_range=(0,highest_price))
    future_price = minmax_scale(future_price, feature_range=(0,highest_price))
    plt.plot(future_price, 'r', data_result, 'b')
    # plt.title(("Real and predicted price of " + company_name + " stock"))
    plt.title(("Real and predicted price of "+Variables.company_name[company_enum]+" stock"))
    plt.xlabel('Time [days]')
    plt.ylabel('Price [$]')
    plt.legend(['Predicted price', 'Real price'])
    # plt.figure(dpi=300)
    # plt.plot(data_result)
    # plt.show()
    plt.savefig('plots/'+Variables.company_name[company_enum])
    plt.clf()

if __name__ == "__main__":
    # PLACEHOLDER
    print('something')
    
    # chosen_data = Data(company_enum)
    # highest_price = chosen_data.prepare_arrays()
    # data_prediction, data_result = chosen_data.reshape_data()
    network = NeuralNetwork()
    # network.build_model(data_prediction)
    # network.evaluate_model(data_prediction, data_result)
    # network.save_model('model7')
    network.load_model('model7')

    for i in range(0,6):
        company_enum = i
        chosen_data1 = Data(company_enum)
        highest_price = chosen_data1.prepare_arrays()
        data_prediction, data_result = chosen_data1.reshape_data()
        
        future_prices = network.predict_prices(data_prediction)
        print_results(future_prices, data_result, highest_price)

    a = QApplication(argv)
    main_window = MainWindow()
    main_window.start()
    a.exec()
 
