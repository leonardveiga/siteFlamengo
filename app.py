#Aplicação na porta 8080 - Leonardo Veiga
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def siteFlamengo():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
