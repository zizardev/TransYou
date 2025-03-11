from flask import Flask, render_template, request, session
from reverso_context_api import Client

app = Flask(__name__)
app.secret_key = "секретный_ключ"
client = Client("en", "ru")

@app.route('/', methods=['GET', 'POST'])
def home():
    text_translate = " "
    if request.method == 'POST':
      if "reset" in request.form: 
        session.clear()
        
      else:
        text = request.form['text_input']
        text_translate = translate(text)
    return render_template('index.html', text_translate=text_translate)

    
def translate(text):
    text_translate = " "
    for word in list(client.get_translations(text)):
        text_translate += word + "," + "\n"
    return text_translate
    
if __name__ == '__main__':
    app.run(debug=True, port=5050)