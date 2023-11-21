from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'user'
usuarios = {'juan': 'admin', 'pepe': 'user'}

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        tarros_total = cantidad_tarros * 9000

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_descuento = tarros_total - (tarros_total * descuento)
        descuento_pesos = tarros_total * descuento

        resultado = {
            'nombre': nombre,
            'tarros_total': tarros_total,
            'descuento': descuento_pesos,
            'total_descuento': total_descuento
        }

    return render_template('ejercicio1.html', resultado=resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None

    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']

        if nombre in usuarios and usuarios[nombre] == contraseña:
            session['nombre'] = nombre
            if nombre == 'juan':
                mensaje = 'Bienvenido administrador juan'
            elif nombre == 'pepe':
                mensaje = 'Bienvenido usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrecta'

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)