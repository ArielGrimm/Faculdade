from flask import Flask, request

app = Flask(__name__)

@app.route("/",methods=['POST'])
def index():
    """
    dados = request.args
     
    if dados['nome'] == "zezinho":
        return "OK"
    else:
        return "invalido!!!" 
    """
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    datanascimento = request.form.get('datanascimento')
    chocolate = request.form.get('chocolate')
    coquinha = request.form.get('coquinha')
    sexo = request.form.get('sexo')
    return f"<h1>{usuario}</h1><h1>{senha}</h1> \
        {datanascimento}Chocolate: {chocolate} \
        Coquinha: {coquinha} Sexo: {sexo}"
@app.route("/formulario")
def formulario():
    return '''
        <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulário</title>
    </head>
    <body>
        <form action="http://localhost:5000/" method="POST">
            <fieldset>
                <label for="txtusuario">Usuario</label>
                <input type="email"
                    id="txtusuario"
                    name="usuario"
                    placeholder="Digite seu usuário">
            </fieldset>
            <fieldset>
                <label for="txtsenha">Senha</label>
                <input type="password"
                    id="txtsenha"
                    name="senha"
                    placeholder="Digite sua senha">
            </fieldset>
            <fieldset>
                <input type="date" name="datanascimento" required>
            </fieldset>
            <fieldset>
                <input type="checkbox" name="chocolate">Chocolate
                <input type="checkbox" name="coquinha">Coca-Cola
            </fieldset>
            <fieldset>
                <input type="radio" name="sexo" value="masc">Masculino
                <input type="radio" name="sexo" value="fem">Feminino
            </fieldset>
            <fieldset>
                <input type="text" name="textofixo"
                value="Ta vendo que não altera"
                readonly="readonly" disabled>
            </fieldset>            
            <!--
                Versão antiga HTML:
                <input type="submit">  
            -->
            <button type="submit">Enviar</button> <!-- Versão do HTML 5 -->
        </form>
    </body>
</html>
    '''