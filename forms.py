from wtforms import Form
from wtforms import StringField,TextAreaField
from wtforms import validators
class FakeNewsForm(Form):
   
    news_title = StringField('title',
    [ 
        validators.length(min=10 , message = 'El titulo es demasiado corto'),
        validators.Required()
        ])
    news_text =  TextAreaField('text',
    [
        validators.length(min = 50, message='El texto es demasiado corto'),
        validators.Required(message = 'El texto es necesario' )
        ])
    

# from predict import predict

# predict("(Foto: Reuters / David McNew) Ex conversaciones MLB jugador Curt Schilling con un reportero en la Exposición de Entretenimiento Electrónico, o E3, en Los Ángeles, California 9 de junio de 2011. Schilling empresa cabezas de videojuegos 38 Studios, que es la liberación de su primer juego en línea.ESPN ha fregado a cabo uno de los momentos más definitorios de la Serie Mundial de playoffs de los Medias Rojas de Boston 2004 que involucren lanzador controvertido y recientemente despedido analista de ESPN, Curt Schilling y su famoso calcetín con sangre de un documental que se emitió durante el fin de semana.La noche del domingo, ESPN transmitió el 2010 30 para 30 documental titulado Cuatro días en octubre. El documental se centra en los Medias Rojas del 2004, que se convirtió en el primer equipo de la MLB para volver batalla de una desventaja de tres juegos en una serie de playoffs de siete juegos cuando vencieron a los rivales Yankees de Nueva York en la Serie de Campeonato de la Liga Americana para avanzar al Mundial Serie.Cuando el documental jugó en ESPN 2 en esta ocasión, la cadena deportiva deja fuera una parte muy integral del documental que el rendimiento más destacado de Schilling en el sexto juego de la serie.ampliar | Colapso (Screengrab: YouTube / MLB) calcetín ensangrentado de Curt Schilling de Juego 6 de la liga del campeonato americana de 2004 entre los Yankees de Nueva York y los Medias Rojas de Boston.Schilling, un conservador que recientemente fue despedido por ESPN para un controvertido mensaje de Facebook que expresó sus puntos de vista sobre la ley baño transgénero de Carolina del Norte, lanzó siete sólidas entradas, permitió sólo una carrera en el trato con una lesión de tobillo y una notable calcetín sangre.Su actuación en el Juego 6 mantuvo a los Medias Rojas de ser eliminados y los llevó a un séptimo y último partido de la serie.Según The Washington Post, el recuento de Juego 6 dura alrededor de 17 minutos en el documental y ESPN necesaria para cortar el documental con el fin de hacer que encaje entre su intervalo de tiempo designado - después del partido un colegio de softball y antes de la noche del domingo Yankees vs. Medias rojas de juego mostrado en ESPN a las 8 pm")
