import keras
from keras import Sequential
from keras.layers import Dense
import numpy as np
from keras import backend as K


def normalize_over_axis1(arr2d):
    for i in range(arr2d.shape[0]):
        hori_sum = sum(arr2d[i])
        if hori_sum!= 0 : arr2d[i] = (arr2d[i])/hori_sum

def build_model(layers_sizes, activation ):
    model = Sequential()
    model.add(Dense(layers_sizes[1], input_dim=layers_sizes[0],activation = activation))
    for i in range(2,len(layers_sizes)):
        model.add(Dense(layers_sizes[i], activation = activation))
    model.compile(loss='mse', optimizer=keras.optimizers.Adam())
    return model

def train(model,epochs,vectors):
    model.fit(vectors,vectors,epochs=epochs)

def get_result_points(model, vectors):
    middle_layer=model.layers[int(len(model.layers) / 2 - 1)]
    input_layer=model.layers[0]
    mapping_function = K.function([input_layer.input], [middle_layer.output])
    points = mapping_function(vectors)[0]
    return points

def process(config, data, epochs, activation, layers_sizes, train_perc):
    model = build_model(layers_sizes,activation)

    train_mask = np.random.rand(data.shape[0]) < train_perc
    data.loc[train_mask,'sampled'] = True
    data.loc[~train_mask,'sampled'] = False

    train_vectors = np.array(data[train_mask]['vector'].to_list()).astype(np.float32)
    normalize_over_axis1(train_vectors)
    np.random.shuffle(train_vectors)
    train(model,epochs,train_vectors)

    predict_list = []
    for i in range(data.shape[0]):
        if data['sampled'][i]:
            predict_list.append(data['vector'][i])
    predict_vectors = np.array(predict_list).astype(np.float32)
    normalize_over_axis1(predict_vectors)
    points = get_result_points(model, predict_vectors)
    pointer = 0
    data['a0'] = 0
    data['a1'] = 0
    data['a2'] = 0
    for i in range(data.shape[0]):
        if data['sampled'][i]:
            for c in range(len(points[pointer])):
                data.loc[i,'a'+str(c)] = points[pointer][c]
            pointer+=1

    print('autoencoder done')