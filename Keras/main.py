# -*- coding: utf-8 -*-

import numpy as np
from tensorflow import keras

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = np.array(x_train) / 255
x_test = np.array(x_test) / 255

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

#Define uma rede neural sequencial
lenet = keras.Sequential()
#Define uma camada de convolução 
lenet.add(keras.layers.Conv1D(filters=6, 
                        kernel_size=3, 
                        activation='relu', 
                        use_bias=True,
                        input_shape=(28,28)))
#Define uma camada de pooling 
lenet.add(keras.layers.MaxPooling1D(strides=2,
                                    pool_size=2))
#Define uma camada de convolução 
lenet.add(keras.layers.Conv1D(filters=16, 
                        kernel_size=3, 
                        activation='relu'))
#Define uma camada de pooling
lenet.add(keras.layers.MaxPooling1D(strides=2,
                                    pool_size=2))
#Transformação de matrizes em um vetor de entrada para uma MLP
lenet.add(keras.layers.Flatten())
#Define uma camada de uma MLP com 120 neurônios
lenet.add(keras.layers.Dense(units=120, activation='relu'))
#Define uma camada de uma MLP com 84 neurônios
lenet.add(keras.layers.Dense(units=84, activation='relu'))
#Define uma camada de uma MLP com 10 neurônios
lenet.add(keras.layers.Dense(units=10, activation = 'softmax'))

#Definições de hiper parâmetro
lenet.compile(
    loss=keras.losses.categorical_crossentropy,
    optimizer=keras.optimizers.Adadelta(),
    metrics=['accuracy']
)

lenet.fit(x_train, y_train, epochs=10, batch_size=128)

score = lenet.evaluate(x_test, y_test, verbose=0)
print('Final loss:', score[0])
print('Final acc:', score[1])