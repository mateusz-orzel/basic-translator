from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/',methods = ['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/translate',methods = ['POST','GET'])
def translate():
    text = ""
    translation = ""
    if request.method == 'POST':
        text = request.form['from-text']
        translation = text[::-1]
        return render_template('translate.html', text=text, translation = translation)
    return render_template('translate.html')

if __name__ == '__main__':
    app.run(debug=True)
