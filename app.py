from flask import Flask, render_template, request
from PIL import Image
import os

# Importando os filtros personalizados
import filtros

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/processed'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        filtro_nome = request.form.get('filtro')
        file = request.files['imagem']

        if file and file.filename.endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(img_path)

            img = Image.open(img_path)

            # Selecionar o filtro a partir do nome
            filtros_disponiveis = {
                'negativo': filtros.filtro_negativo,
                'mediana': filtros.filtro_mediana,
                'gaussiana': filtros.filtro_gaussiano,
                'pb': filtros.filtro_pb,
                'contorno': filtros.filtro_contorno
            }

            func_filtro = filtros_disponiveis.get(filtro_nome, lambda x: x)
            img_processada = func_filtro(img)

            processed_path = os.path.join(PROCESSED_FOLDER, file.filename)
            img_processada.save(processed_path)

            return render_template(
                'index.html',
                original=img_path,
                processada=processed_path,
                filtro=filtro_nome
            )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)