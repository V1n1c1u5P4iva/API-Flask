import pandas as pd
from flask import jsonify, Flask
from pyngrok import ngrok
import random as r

# Substitua 'YOUR_AUTHTOKEN' pelo seu token de autenticação ngrok
ngrok.set_auth_token('YOUR_AUTHTOKEN')

app = Flask(__name__)

@app.route("/")
def home():
    return "<marquee><h3> TO CHECK INPUT, ADD '/input' TO THE URL AND TO CHECK OUTPUT, ADD '/output' TO THE URL.</h3></marquee>"

@app.route("/input")
def input():
    # Lê a planilha Excel
    df = pd.read_excel('Digite o caminho')
    
    # Converte o DataFrame para JSON
    json_data = df.to_json(orient='records', indent=4)
    
    return jsonify(json_data)

@app.route('/output', methods=['GET', 'POST'])
def predJson():
    pred = r.choice(["positive", "negative"])
    
    d = {
        "name": "Teste",
        "surname": "API",
        "idade": 60,
        "prediction": pred
    }
    return jsonify(d)

if __name__ == '__main__':
    # Inicia o túnel ngrok
    public_url = ngrok.connect(5000)
    print(f" * ngrok URL: {public_url}")
    app.run()
