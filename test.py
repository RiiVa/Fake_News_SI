# from keras import layers
# from keras import models
from recollect import GetNews
# from keras.preprocessing.text import Tokenizer
# from keras.preprocessing.sequence import pad_sequences
import numpy as np
import json, codecs
import text_metadata
from recollect import data,labels,text_metadata,max_words,x_test, y_test
from TI_CNN_model import create_model


# def saveHist(path, history):
# 	with codecs.open(path, 'w', encoding='utf-8') as f:
# 		json.dump(history, f, separators=(',',':'), sort_keys = True, indent = 4)


def loadHist(path):
	n = {}
	if os.path.exists(path):
		with codecs.open(path,'r',encoding='utf-8') as f:
			n = json.loads(f.read())
	return n

def saveHist(path, history):
	new_hist = {}
	for key in list(history.history.keys()):
		print(key)
		if type(history.history[key]) == np.ndarray:
			new_hist[key] = history.history[key].tolist()
		elif type(history.history[key])== list:
			if type(history.history[key][0]) == np.float64:
				new_hist[key] = list(map(float, history.history[key]))
		else:
			print('llego')
			new_hist[key] = history.history[key].tolist()
	# print(new_hist)
	print(new_hist.keys())
	with codecs.open(path, 'w', encoding='utf-8') as f:
 		json.dump(new_hist, f, separators=(',',':'), sort_keys = True, indent = 4)


sdata=data.shape[1]
stext_metadata=text_metadata.shape[1]
samples=data.shape[0]
training_samples=int(samples*0.8)




text_implicit_train = data[:training_samples]
text_explicit_train = text_metadata[:training_samples]
y_train = labels[:training_samples]

# print(y_train.sum())

model=create_model(sdata,stext_metadata,max_words)
print(model.summary())

model.load_weights('pre_trained_20000_spanish_model.h5')
# history = loadHist('history.json')
# history=model.fit([text_implicit_train,text_explicit_train],y_train,
# 					epochs=30,
# 					batch_size=64,
# 					validation_split=0.2)
# model.save_weights('pre_trained_20000_spanish_model.h5')

# print(history.history)
# print(history.history.keys())
# saveHist('history.json',history)
# loss, accuracy, f1_score, precision,recall = model.evaluate([text_implicit_train,text_explicit_train],y_train)
# print(f1_score, '<------------- f1_score')
# print(loss, '<------------- loss')
# print(accuracy, '<------------- score')





"""
Construye los coeficientes de embeddings

glove_dir = '/Users/fchollet/Downloads/glove.6B'

embeddings_index = {}
f = open(os.path.join(glove_dir, 'glove.6B.100d.txt'))
for line in f:
	values = line.split()
	word = values[0]
	coefs = np.asarray(values[1:], dtype = 'float32')
	embeddings_index[word] = coefs
f.close()
print('Found %s word vectors.' % len(embeddings_index))


"""


# embedding_dim = 100

# embedding_matrix = np.zeros((max_words, embedding_dim))
# for word, i in word_index.items():
# 	if i < max_words:
# 		embedding_vector = embeddings_index.get(word)
# 		if embedding_vector is not None:
# 			embedding_matrix[i] = embedding_vector

# print(history.history)

# print(history.history)


"""
dict_keys(['val_loss', 'val_mean_absolute_error', 'val_binary_accuracy', 'val_categorical_accuracy',
 'val_sparse_categorical_accuracy', 'val_cosine_proximity', 'loss', 'mean_absolute_error', 'binary_accuracy',
  'categorical_accuracy', 'sparse_categorical_accuracy', 'cosine_proximity'])

"""


# top_k = history.history['top_k_categorical_accuracy']
# val_top_k = history.history['val_top_k_categorical_accuracy']

# sparse_top_k = history.history['sparse_top_k_categorical_accuracy']
# val_sparse_top_k = history.history['val_sparse_top_k_categorical_accuracy']


# print('accuracy')
# print(acc)
# print('val_accuracy')
# print(val_acc)
# print('loss')
# print(loss)
# print('val_loss')
# print(val_loss)

# acc = history.history['acc']
# val_acc = history.history['val_acc']

# loss = history.history['loss']
# val_loss = history.history['val_loss']

# f1 = history.history['f1_m']
# val_f1 = history.history['val_f1_m']

# precision_m = history.history['precision_m']
# val_precision_m = history.history['val_precision_m']

# recall_m = history.history['recall_m']
# val_recall_m = history.history['val_recall_m']

# import matplotlib.pyplot as plt
# epochs = range(1, len(acc) + 1)

# plt.plot(epochs, acc, 'bo', label='Training acc')
# plt.plot(epochs, val_acc,'b', label= 'Validation acc')
# plt.title('Training and validation accuracy')
# plt.legend()

# plt.figure()

# plt.plot(epochs, loss, 'bo', label = 'Training loss')
# plt.plot(epochs, val_loss, 'b', label= 'Validation loss')
# plt.title('Training and validation loss')
# plt.legend()

# plt.figure()

# plt.plot(epochs, f1, 'bo', label='Training f1')
# plt.plot(epochs, val_f1,'b', label= 'Validation f1')
# plt.title('Training and validation f1 score')
# plt.legend()

# plt.figure()

# plt.plot(epochs, precision_m, 'bo', label='Training precision_m')
# plt.plot(epochs, val_precision_m,'b', label= 'Validation precision_m')
# plt.title('Training and validation precision_m')
# plt.legend()

# plt.figure()

# plt.plot(epochs, recall_m, 'bo', label='Training recall_m')
# plt.plot(epochs, recall_m,'b', label= 'Validation recall_m')
# plt.title('Training and validation recall_m')
# plt.legend()

# plt.show()