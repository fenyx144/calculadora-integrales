# Calculadora de Integrales Definidas 🧮

Este proyecto es una aplicación web para calcular integrales definidas utilizando **Flask** y **SymPy** en Python. La aplicación permite al usuario ingresar una función matemática, el límite inferior y superior, y obtener el resultado de la integral.

## Funcionalidades 🚀

- **Cálculo de integrales definidas**: Ingrese una función matemática y los límites de integración para obtener el valor de la integral definida.
- **Interfaz simple**: Una página web sencilla con campos para ingresar la función y los límites de integración.
- **Resultados claros**: La aplicación muestra el resultado de la integral, junto con el valor calculado.

## Requisitos 📦

Para ejecutar este proyecto, necesitas tener instalado lo siguiente:

- Python 3.x
- Flask
- SymPy

## Instalación 🔧

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu-usuario/calculadora-integrales.git
    ```

2. Accede al directorio del proyecto:

    ```bash
    cd calculadora-integrales
    ```

3. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    ```

4. Activa el entorno virtual:

    - En Windows:

      ```bash
      .\venv\Scripts\activate
      ```

    - En macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso 🖥️

1. Inicia el servidor de desarrollo de Flask:

    ```bash
    python app.py
    ```

2. Abre tu navegador y visita [http://127.0.0.1:5000](http://127.0.0.1:5000) para usar la calculadora.

3. Ingresa la función, el límite inferior y el límite superior, y presiona "Calcular" para obtener el resultado de la integral definida.

## Ejemplo de uso 📊

- Función: `x**2`
- Límite inferior: `0`
- Límite superior: `2`

Resultado: `8/3 ≈ 2.667`

## Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si tienes alguna mejora, corrección o nueva funcionalidad que agregar, no dudes en abrir un **pull request**.

1. Haz un **fork** de este repositorio.
2. Crea una nueva rama para tu funcionalidad: `git checkout -b feature/nueva-funcionalidad`.
3. Realiza tus cambios y haz un commit: `git commit -m 'Agrega nueva funcionalidad'`.
4. Haz un push a tu rama: `git push origin feature/nueva-funcionalidad`.
5. Abre un pull request.

## Demo 📜

[Demo en heroku]()