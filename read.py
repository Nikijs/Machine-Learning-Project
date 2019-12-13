# Adapted from: https://docs.python.org/3/library/gzip.html
import gzip
import numpy as np
import keras as kr

# Start a neural network, building it by layers.
model = kr.models.Sequential()

# Add a hidden layer with 1000 neurons and an input layer with 784.
model.add(kr.layers.Dense(units=600, activation='linear', input_dim=784))
model.add(kr.layers.Dense(units=400, activation='relu'))
# Add a three neuron output layer.
model.add(kr.layers.Dense(units=10, activation='softmax'))
#read data from MNIST dataset
with gzip.open('MNIST/train-images-idx3-ubyte.gz', 'rb') as f:
    train_img = f.read()

with gzip.open('MNIST/train-labels-idx1-ubyte.gz', 'rb') as f:
    train_lbl = f.read()
#Create numPy arrays and reshape them
train_img = ~np.array(list(train_img[16:])).reshape(60000, 28, 28).astype(np.uint8) / 255.0
train_lbl =  np.array(list(train_lbl[ 8:])).astype(np.uint8)

inputs = train_img.reshape(60000, 784)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])



# For encoding categorical variables.
import sklearn.preprocessing as pre

encoder = pre.LabelBinarizer()
encoder.fit(train_lbl)
outputs = encoder.transform(train_lbl)

print(train_lbl[0], outputs[0])

for i in range(10):
    print(i, encoder.transform([i]))

#poches is the amount of times the test is carried out
model.fit(inputs, 
          outputs,  
          epochs=5,
          ) 
#https://www.tensorflow.org/tutorials/keras/save_and_load

# Save the entire model to a HDF5 file.
model.save('my_model.h5') 