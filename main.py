from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta

app = Flask(__name__)

lista_usuarios = ['Lucas', 'Gabriel', 'Fátima', 'Vinicius', 'Cláudia']

app.config['SECRET_KEY'] = 'e2f8274d48dc01d27c9ab6b844109580'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route("/login")
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)

if __name__ == '__main__':
    app.run(debug=True)