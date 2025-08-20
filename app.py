from flask import Flask, request, render_template_string

app = Flask(__name__)

# Plantilla HTML con CSS moderno
HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Cloud Calculator ☁️</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #1CB5E0 0%, #000851 100%);
            color: #333;
            text-align: center;
            padding: 40px;
        }
        h1 {
            color: white;
            margin-bottom: 20px;
            font-size: 2.5rem;
        }
        .container {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }
        .card {
            background: white;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            padding: 20px;
            width: 320px;
            transition: transform 0.2s;
        }
        .card:hover {
            transform: scale(1.05);
        }
        input, select, button {
            margin: 10px 0;
            padding: 10px;
            font-size: 16px;
            width: 90%;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        button {
            background: #1CB5E0;
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }
        button:hover {
            background: #000851;
        }
        .resultado {
            margin-top: 20px;
            padding: 15px;
            background: #f1f1f1;
            border-left: 5px solid #1CB5E0;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 600;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>☁️ Cloud Calculator</h1>
    <div class="container">

        <!-- Calculadora -->
        <div class="card">
            <h2>Operaciones Matemáticas</h2>
            <form method="get" action="/calculate">
                <input type="number" step="any" name="a" placeholder="Número 1" required>
                <select name="op">
                    <option value="add">➕ Suma</option>
                    <option value="sub">➖ Resta</option>
                    <option value="mul">✖️ Multiplicación</option>
                    <option value="div">➗ División</option>
                </select>
                <input type="number" step="any" name="b" placeholder="Número 2" required>
                <button type="submit">Calcular</button>
            </form>
        </div>

        <!-- Conversor -->
        <div class="card">
            <h2>Conversión de Temperatura 🌡️</h2>
            <form method="get" action="/convert">
                <input type="number" step="any" name="temp" placeholder="Temperatura" required>
                <select name="scale">
                    <option value="C">Celsius → Fahrenheit</option>
                    <option value="F">Fahrenheit → Celsius</option>
                </select>
                <button type="submit">Convertir</button>
            </form>
        </div>

    </div>

    {% if resultado %}
    <div class="resultado">{{ resultado }}</div>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/calculate")
def calculate():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        op = request.args.get("op")

        if op == "add":
            result = a + b
            symbol = "+"
        elif op == "sub":
            result = a - b
            symbol = "-"
        elif op == "mul":
            result = a * b
            symbol = "×"
        elif op == "div":
            if b == 0:
                return render_template_string(HTML_PAGE, resultado="❌ No se puede dividir por cero")
            result = a / b
            symbol = "÷"
        else:
            return render_template_string(HTML_PAGE, resultado="❌ Operación no válida")

        return render_template_string(HTML_PAGE, resultado=f"{a} {symbol} {b} = {result}")
    except Exception as e:
        return render_template_string(HTML_PAGE, resultado=f"Error: {str(e)}")

@app.route("/convert")
def convert_temperature():
    try:
        temp = float(request.args.get("temp"))
        scale = request.args.get("scale", "C").upper()

        if scale == "C":
            result = (temp * 9/5) + 32
            return render_template_string(HTML_PAGE, resultado=f"{temp} °C = {result:.2f} °F")
        elif scale == "F":
            result = (temp - 32) * 5/9
            return render_template_string(HTML_PAGE, resultado=f"{temp} °F = {result:.2f} °C")
        else:
            return render_template_string(HTML_PAGE, resultado="❌ Escala inválida")
    except Exception as e:
        return render_template_string(HTML_PAGE, resultado=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
