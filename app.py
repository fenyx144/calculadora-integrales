from flask import Flask, render_template, request
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import os
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Obtener la función y el intervalo desde el formulario
    func_str = request.form['function']
    a = float(request.form['a'])
    b = float(request.form['b'])
    
    # Convertir la función de texto a una expresión simbólica
    x = sp.symbols('x')
    func = sp.sympify(func_str)
    
    # Calcular la integral definida
    integral_result = sp.integrate(func, (x, a, b))
    
    # Generar el gráfico
    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = [float(func.subs(x, val)) for val in x_vals]
    
    plt.figure(figsize=(6, 4))
    plt.plot(x_vals, y_vals, label=f'{func_str}')
    plt.fill_between(x_vals, y_vals, where=(x_vals >= a) & (x_vals <= b), color='skyblue', alpha=0.5)
    plt.title(f'Área bajo la curva de {func_str}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()

    # Guardar el gráfico en un archivo en memoria
    img_io = io.BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)
    
    # Codificar la imagen en base64 para mostrarla en el HTML
    img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
    
    # Retornar el resultado y la imagen
    return render_template('index.html', integral_result=integral_result, img_data=img_base64)

if __name__ == '__main__':
    app.run(debug=True)
