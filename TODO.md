# TODO

setup charts in graphics.py using future_prices data

    # chosen_data = Data(company_enum)
    # highest_price = chosen_data.prepare_arrays()
    # data_prediction, data_result = chosen_data.reshape_data()
    network = NeuralNetwork()
    # network.build_model(data_prediction)
    # network.evaluate_model(data_prediction, data_result)
    # # network.save_model('model7')
    network.load_model('model7')

    # generate_graphs()
    for i in range(0,6):
        company_enum = i
        chosen_data = Data(company_enum)
        highest_price = chosen_data.prepare_arrays()
        data_prediction, data_result = chosen_data.reshape_data()
        
        future_prices = network.predict_prices(data_prediction)
        print_results(future_prices, data_result, highest_price)