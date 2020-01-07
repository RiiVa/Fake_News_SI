from flask import Flask
from flask import render_template
from flask import  request
from flask import flash
import sys,os,re
import json, codecs
import forms
# from predict import predict

app = Flask(__name__)
app.__setattr__('sandor','')


@app.route('/', methods = ['GET', 'POST'])
def index():
    news_forms = forms.FakeNewsForm(request.form)
    result = "Primero pase los parametros para comenzar con el algoritmo"
    if request.method == 'POST' and news_forms.validate():
        # print( news_forms.news_title.data)
        
        text = news_forms.news_text.data
        

        with codecs.open("test.json", 'w', encoding='utf-8') as f:
	        json.dump(text, f, separators=(',',':'), sort_keys = True, indent = 4)

        value = app.sandor(text)
        print(value)
        if value > 0.6:
            result = " La noticia es legitima dandonos un score de {}".format(value)
        else : 
            result = " La noticia es falsa dandonos un score de {}".format(value)
        # print(result)
        # result = "termino de calcular"
            


    
    return render_template('index.html', form = news_forms , result = result )




