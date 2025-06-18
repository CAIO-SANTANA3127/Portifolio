from flask import Flask, render_template, request, jsonify, send_from_directory, flash, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# ✅ Chave secreta necessária para sessões e flash messages
app.secret_key = os.urandom(24)  # Gera uma chave segura aleatória a cada execução

# Configurações do servidor de e-mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'pereiracaio2110@gmail.com'
app.config['MAIL_PASSWORD'] = 'oddg pdri fywf quxt'  # Cuidado: não exponha sua senha em código real
app.config['MAIL_DEFAULT_SENDER'] = 'pereiracaio2110@gmail.com'

mail = Mail(app)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para envio de e-mails
@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get("nome")
    email = request.form.get("email")
    mensagem = request.form.get("mensagem")

    if not nome or not email or not mensagem:
        flash("❌ Todos os campos são obrigatórios!", "error")
        return redirect(url_for("index"))

    try:
        msg = Message(
            subject=f"Nova mensagem de {nome}",
            sender=app.config['MAIL_DEFAULT_SENDER'],
            recipients=['pereiracaio2110@gmail.com'],
            body=f"Nome: {nome}\nE-mail: {email}\nMensagem:\n{mensagem}"
        )
        mail.send(msg)
        flash("✅ Mensagem enviada com sucesso!", "success")
        return redirect(url_for("index"))

    except Exception as e:
        flash(f"❌ Erro ao enviar mensagem: {str(e)}", "error")
        return redirect(url_for("index"))

# Rota para servir arquivos estáticos
@app.route('/static/<path:filename>')
def send_static_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == '__main__':
    app.run(debug=True)
