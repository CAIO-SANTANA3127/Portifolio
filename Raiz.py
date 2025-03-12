from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para servir arquivos estáticos
@app.route('/static/<path:filename>')
def send_static_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == '__main__':
    app.run(debug=True)
