# from tensorflow.python.keras.models import Model
from keras.models import Model
from keras import layers
from keras import optimizers
from keras import Input
from keras import metrics
import text_metadata
# from recollect import data,labels
from keras import backend as K

def recall_m(y_true, y_pred):
	true_positives = K.sum(K.round(K.clip(y_true * y_pred,0,1)))
	possible_positives = K.sum(K.round(K.clip(y_true,0 ,1)))
	recall = true_positives / (possible_positives + K.epsilon())
	return recall

def precision_m(y_true, y_pred):
	true_positives = K.sum(K.round(K.clip(y_true * y_pred,0,1)))
	predicted_positives = K.sum(K.round(K.clip(y_pred,0 ,1)))
	precission = true_positives/(predicted_positives + K.epsilon())
	return precission

def f1_m (y_true, y_pred):
	precission = precision_m(y_true,y_pred)
	recall = recall_m(y_true,y_pred)
	return 2*((precission*recall)/(precission+recall+K.epsilon()))


def create_model(text_implicit_size,text_explicit_size,max_words):
    text_input = Input(shape=(text_implicit_size,), dtype='int32', name='text')
    embedded_text = layers.Embedding(max_words, 100)(text_input)
    x = layers.Dropout(0.5)(embedded_text)
    x = layers.Conv1D(10, 7, activation='relu')(x)
    x = layers.MaxPooling1D(2)(x)
    x = layers.Conv1D(10, 7, activation='relu')(x)
    x = layers.GlobalMaxPooling1D()(x)
    # x = layers.Flatten()(x)
    # Con un corpus de 20000 news que tiene el paper se pondria 128 neuronas
    x = layers.Dense(8,activation='relu')(x)
    # x = layers.Dropout(0.2)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dense(1,activation='relu')(x)
    text_explicit=Input(shape=(text_explicit_size,), dtype='float32', name='text_explicit')
    # Con un corpus de 20000 news que tiene el paper se pondria 128 neuronas
    y = layers.Dense(8,activation='relu')(text_explicit)
    y = layers.BatchNormalization()(y)
    y = layers.Dense(1,activation='relu')(y)
                        
    concatenated = layers.concatenate([x, y],axis=-1)
    # Con un corpus de 20000 news que tiene el paper se pondria 128 neuronas
    concatenated_dense = layers.Dense(8,activation='relu')(concatenated)
    concatenated_BN = layers.BatchNormalization()(concatenated_dense)
    concatenated_S = layers.Dense(1,activation='sigmoid')(concatenated_BN)
    model = Model([text_input, text_explicit], concatenated_S)

    model.compile(
                    # optimizer=optimizers.RMSprop(lr=0.001),
                    optimizer='rmsprop',
                    # loss='mse',
                    loss='binary_crossentropy',
                    metrics=['acc',f1_m,precision_m,recall_m])
    return model
# print(model.summary())