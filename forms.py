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
    

