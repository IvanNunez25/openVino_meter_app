# from flask import Flask

# app = Flask(__name__)

# @app.route('/members')
# def members():
#     return {"members": ["member1", "member2", "member3"]}

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/villa/IA/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Crear la carpeta de subidas si no existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/subir', methods=['POST'])
def subir_imagen():
    if 'file' not in request.files:
        print(" NO FILE ")
        return jsonify({'error': 'No se encontró el archivo en la solicitud'}), 400
    
    file = request.files['file']
    
    print( file )
    
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        print(filepath)
        file.save(filepath)
        return jsonify({'message': 'Archivo subido exitosamente', 'filepath': filepath}), 200
    


if __name__ == '__main__':
    app.run(debug=True)