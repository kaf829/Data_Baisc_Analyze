import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, GRU, Conv1D, MaxPooling1D, Flatten, Dense, Dropout
from keras.optimizers import Adam, RMSprop
from keras.callbacks import EarlyStopping
from keras.backend import clear_session
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler

class TimeSeriesModelTrainer:
    def __init__(self, df, target_column='Global_active_power', freq='min'):
        self.df = df
        self.target_column = target_column
        self.freq = freq
        self.scaler = MinMaxScaler()
        self.results = []

    def preprocess(self):
        df_resampled = self.df.resample(self.freq).mean().dropna()
        series = df_resampled[self.target_column].values.reshape(-1, 1)
        self.scaled_series = self.scaler.fit_transform(series)

        total_len = len(self.scaled_series)
        train_size = int(total_len * 0.6)
        val_size = int(total_len * 0.2)

        self.train_data = self.scaled_series[:train_size]
        self.val_data = self.scaled_series[train_size:train_size + val_size]
        self.test_data = self.scaled_series[train_size + val_size:]

    def create_dataset(self, data, look_back):
        X, y = [], []
        for i in range(len(data) - look_back):
            X.append(data[i:i + look_back])
            y.append(data[i + look_back])
        return np.array(X), np.array(y)

    def train(self, look_backs, units_list, batch_sizes, epochs_list, dropouts, optimizers, layer_options, model_types):
        i = 1
        for model_type in model_types:
            for look_back in look_backs:
                X_train, y_train = self.create_dataset(self.train_data, look_back)
                X_val, y_val = self.create_dataset(self.val_data, look_back)
                X_test, y_test = self.create_dataset(self.test_data, look_back)

                X_train = X_train.reshape(-1, look_back, 1)
                X_val = X_val.reshape(-1, look_back, 1)
                X_test = X_test.reshape(-1, look_back, 1)

                for units in units_list:
                    for batch_size in batch_sizes:
                        for epochs in epochs_list:
                            for dropout in dropouts:
                                for opt in optimizers:
                                    for layers in layer_options:
                                        clear_session()
                                        print(f"{i} Training {model_type}: look_back={look_back}, units={units}, "
                                              f"batch={batch_size}, epochs={epochs}, dropout={dropout}, "
                                              f"opt={opt}, layers={layers}")
                                        i += 1
                                        model = Sequential()

                                        if model_type == 'LSTM':
                                            self._add_lstm_layers(model, look_back, units, layers)
                                        elif model_type == 'GRU':
                                            self._add_gru_layers(model, look_back, units, layers)
                                        elif model_type == 'CNN':
                                            self._add_cnn_layers(model, look_back, units, layers)
                                        elif model_type == 'DENSE':
                                            self._add_dense_layers(model, look_back, units, layers)

                                        if dropout > 0.0:
                                            model.add(Dropout(dropout))
                                        model.add(Dense(1))

                                        model.compile(optimizer=opt, loss='mse')
                                        early_stop = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

                                        model.fit(X_train, y_train,
                                                  epochs=epochs,
                                                  batch_size=batch_size,
                                                  validation_data=(X_val, y_val),
                                                  callbacks=[early_stop],
                                                  verbose=0)

                                        pred = model.predict(X_test)
                                        pred_inv = self.scaler.inverse_transform(pred)
                                        y_test_inv = self.scaler.inverse_transform(y_test.reshape(-1, 1))
                                        mae = mean_absolute_error(y_test_inv, pred_inv)
                                        print(f"✅ Done → MAE: {mae:.4f}")

                                        self.results.append({
                                            'model': model_type,
                                            'look_back': look_back,
                                            'units': units,
                                            'batch_size': batch_size,
                                            'epochs': epochs,
                                            'dropout': dropout,
                                            'optimizer': opt,
                                            'layers': layers,
                                            'MAE': mae
                                        })

        return pd.DataFrame(self.results).sort_values(by='MAE')

    def _add_lstm_layers(self, model, look_back, units, layers):
        if layers == 1:
            model.add(LSTM(units, input_shape=(look_back, 1)))
        elif layers == 2:
            model.add(LSTM(units, return_sequences=True, input_shape=(look_back, 1)))
            model.add(LSTM(units // 2))
        elif layers == 3:
            model.add(LSTM(units, return_sequences=True, input_shape=(look_back, 1)))
            model.add(LSTM(units, return_sequences=True))
            model.add(LSTM(units // 2))

    def _add_gru_layers(self, model, look_back, units, layers):
        if layers == 1:
            model.add(GRU(units, input_shape=(look_back, 1)))
        elif layers == 2:
            model.add(GRU(units, return_sequences=True, input_shape=(look_back, 1)))
            model.add(GRU(units // 2))
        elif layers == 3:
            model.add(GRU(units, return_sequences=True, input_shape=(look_back, 1)))
            model.add(GRU(units, return_sequences=True))
            model.add(GRU(units // 2))

    def _add_cnn_layers(self, model, look_back, units, layers):
        model.add(Conv1D(filters=units, kernel_size=3, activation='relu', input_shape=(look_back, 1)))
        model.add(MaxPooling1D(pool_size=2))
        if layers >= 2:
            model.add(Conv1D(filters=units // 2, kernel_size=3, activation='relu'))
            model.add(MaxPooling1D(pool_size=2))
        if layers == 3:
            model.add(Conv1D(filters=units // 4, kernel_size=3, activation='relu'))
        model.add(Flatten())

    def _add_dense_layers(self, model, look_back, units, layers):
        model.add(Flatten(input_shape=(look_back, 1)))
        for _ in range(layers):
            model.add(Dense(units, activation='relu'))
