from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, LSTM
from variables import Variables


class NeuralNetwork:

    # def __init__(self):
    #     self.model = Sequential()

    def build_model(self, data_prediction):
        self.model = Sequential()
        self.model.add(LSTM(50, return_sequences=True, input_shape=(data_prediction.shape[1], 1)))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(50, return_sequences=False))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(1))

        # loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

        self.model.compile(optimizer='adam',
                      loss='mean_squared_error')

    def evaluate_model(self, data_prediction, data_result):
        self.model.fit(data_prediction, data_result, batch_size=1, epochs=Variables.epochs)
        print(self.model.evaluate(data_prediction,  data_result, verbose=2))

    def save_model(self, name):
        return self.model.save('models/' + name)

    def load_model(self, name):
        self.model = load_model('models/' + name)

    def predict_prices(self, data_prediction):
        return self.model.predict(data_prediction)
