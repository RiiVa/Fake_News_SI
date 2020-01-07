import numpy as np
from recollect import TextMetadata,Vectorize2
from TI_CNN_model import create_model
import sys,os,re
import json, codecs

from server_flask import app

from tensorflow.python.keras.backend import set_session
import tensorflow as tf
import tensorflow._api.v1.config as config
tf_config = config
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto( allow_soft_placement=True, log_device_placement=True))
graph = tf.get_default_graph()
set_session(sess)




model = create_model(1494,7,100)
# print(model.summary())

model.load_weights('pre_trained_20000_spanish_model.h5')

path = "tokenizer_json.json"
if os.path.exists(path):
    # print("entro aqui")
    with codecs.open(path,'r',encoding='utf-8') as f:
	    json_string = json.loads(f.read())
# print(json_string)

def predict(text):
    temp = []
    temp.append(text)
    
    x_test_vect = Vectorize2(temp,json_string)
    x_test = TextMetadata(temp)
    # print(x_test)
    print("Ahora si")
    print(x_test_vect)
    print(x_test)

    global sess
    global graph    
    with graph.as_default():
        set_session(sess)
        value = model.predict([x_test_vect, x_test] ,verbose=1)
    return value[0][0]
    # with codecs.open("result.json", 'w', encoding='utf-8') as f:
	#     json.dump(str(value[0][0]), f, separators=(',',':'), sort_keys = True, indent = 4)
    # print(value)
    # model.
    # print("resultado --------")
# a = predict("(Foto: Reuters / David McNew) Ex conversaciones MLB jugador Curt Schilling con un reportero en la Exposición de Entretenimiento Electrónico, o E3, en Los Ángeles, California 9 de junio de 2011. Schilling empresa cabezas de videojuegos 38 Studios, que es la liberación de su primer juego en línea.ESPN ha fregado a cabo uno de los momentos más definitorios de la Serie Mundial de playoffs de los Medias Rojas de Boston 2004 que involucren lanzador controvertido y recientemente despedido analista de ESPN, Curt Schilling y su famoso calcetín con sangre de un documental que se emitió durante el fin de semana.La noche del domingo, ESPN transmitió el 2010 30 para 30 documental titulado Cuatro días en octubre. El documental se centra en los Medias Rojas del 2004, que se convirtió en el primer equipo de la MLB para volver batalla de una desventaja de tres juegos en una serie de playoffs de siete juegos cuando vencieron a los rivales Yankees de Nueva York en la Serie de Campeonato de la Liga Americana para avanzar al Mundial Serie.Cuando el documental jugó en ESPN 2 en esta ocasión, la cadena deportiva deja fuera una parte muy integral del documental que el rendimiento más destacado de Schilling en el sexto juego de la serie.ampliar | Colapso (Screengrab: YouTube / MLB) calcetín ensangrentado de Curt Schilling de Juego 6 de la liga del campeonato americana de 2004 entre los Yankees de Nueva York y los Medias Rojas de Boston.Schilling, un conservador que recientemente fue despedido por ESPN para un controvertido mensaje de Facebook que expresó sus puntos de vista sobre la ley baño transgénero de Carolina del Norte, lanzó siete sólidas entradas, permitió sólo una carrera en el trato con una lesión de tobillo y una notable calcetín sangre.Su actuación en el Juego 6 mantuvo a los Medias Rojas de ser eliminados y los llevó a un séptimo y último partido de la serie.Según The Washington Post, el recuento de Juego 6 dura alrededor de 17 minutos en el documental y ESPN necesaria para cortar el documental con el fin de hacer que encaje entre su intervalo de tiempo designado - después del partido un colegio de softball y antes de la noche del domingo Yankees vs. Medias rojas de juego mostrado en ESPN a las 8 pm")
# b = predict("Huracán Sandy Live Feed y abierto Tema De los lectores que esta historia es un hecho. Añadir su granito de arena. (Antes de que sea Noticias) Hay simplemente demasiado para la cubierta sobre el huracán de arena y de empuje hacia el Atlántico medio y Nueva York / Nueva Jersey, así que vamos a poner un hilo de discusión y el blog en vivo. Para empezar aquí está una transmisión en vivo (a través de Google) de The Weather Channel: Decir sus historias y compartir fotos de abajo. Fuente:")
# print(a)
# print(str(a[0][0]))

# if os.path.exists("test.json"):
#     # print("entro aqui")
#     with codecs.open("test.json",'r',encoding='utf-8') as f:
# 	    test = json.loads(f.read())

# print(predict(test))




app.sandor = predict


if __name__ == '__main__':
    app.run(debug = True)