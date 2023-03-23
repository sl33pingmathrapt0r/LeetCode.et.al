import helper
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout
from keras.optimizers import adam
from keras.losses import mean_squared_error

df = pd.read_csv('Neural Networks/Python Stock Prediction Project/TSLA.csv')
df = df['Open'].values
df = df.reshape(-1, 1)

# setup datasets
dataset_train = np.array(df[:int(df.shape[0]*0.8)])
dataset_test = np.array(df[int(df.shape[0]*0.8):])

# scale the values
scaler = MinMaxScaler(feature_range=(0,1))
dataset_train = scaler.fit_transform(dataset_train)
dataset_test = scaler.transform(dataset_test)

# use the 'create_dataset' function here on the datasets to create train/test datasets
x_train, y_train = helper.create_dataset(dataset_train)
x_test, y_test = helper.create_dataset(dataset_test)

# reshape the 'x_train' and 'x_test' datasets
# todo
x_train= x_train.reshape(*x_train.shape, 1)
x_test= x_test.reshape(*x_test.shape, 1)

# implement the 'Sequential' model here
model= Sequential()
model.add(LSTM(4, input_shape=x_train.shape[1:], return_sequences= True))
model.add(Dropout(0.2))
model.add(LSTM(4, return_sequences= True))
model.add(Dropout(0.2))
model.add(Dense(1))

# compile the model, fit it, and then predict the values for 'x_test'
# todo
model.compile(
    optimizer= adam.Adam(), 
    loss= mean_squared_error
)

history= model.fit(
    x_train,
    y_train, 
    epochs=5, 
    batch_size= 16, 
    verbose= 0
)

predictions= model.predict(x_test)
# finally print the last column of the 'predictions' array and the model summary
# todo
for i in range(len(predictions)): print(predictions[i][-1])
# print(predictions[:,:,-1])
model.summary()