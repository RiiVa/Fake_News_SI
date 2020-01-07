from flask import Flask
from flask import render_template
from flask import  request
from flask import flash

import forms

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def index():
    news_forms = forms.FakeNewsForm(request.form)
    if request.method == 'POST' and news_forms.validate():
        print( news_forms.news_title.data)



    return render_template('index.html', form = news_forms  )
if __name__ == '__main__':
    app.run(debug = True)