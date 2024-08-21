import os
import pandas as pd
from flask import jsonify, Flask
from pyngrok import ngrok
import random as r

# Obtenha o token de autenticação do ngrok e a porta do ambiente
ngrok_auth_token = os.getenv('NGROK_AUTH_TOKEN')
excel_file_path = os.getenv('EXCEL_FILE_PATH')
ngrok_port = os.getenv('NGROK_PORT', 5000)  # Porta padrão é 5000 se não for especificada

if not ngrok_auth_token or not excel_file_path:
    raise ValueError("As variáveis de ambiente NGROK_AUTH_TOKEN e EXCEL_FILE_PATH devem ser definidas.")

# Configura o token de autenticação do ngrok
ngrok.set_auth_token(ngrok_auth_token)

app = Flask(__name__)

@app.route("/")
def home():
    return "<marquee><h3> TO CHECK INPUT, ADD '/input' TO THE URL AND TO CHECK OUTPUT, ADD '/output' TO THE URL.</h3></marquee>"

@app.route("/input")
def input():
    # Lê a planilha Excel
    df = pd.read_excel(excel_file_path)
    
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
    public_url = ngrok.connect(ngrok_port)
    print(f" * ngrok URL: {public_url}")
    app.run(port=ngrok_port)
