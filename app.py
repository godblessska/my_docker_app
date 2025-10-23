from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        a = float(request.form['a'])
        b = float(request.form['b'])
        op = request.form['operation']
    except (KeyError, ValueError):
        return render_template('index.html', error="Please enter valid numbers.")

    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        if b == 0:
            return render_template('index.html', error="Division by zero!")
        result = a / b
    else:
        return render_template('index.html', error="Unknown operation.")

    return render_template('index.html', result=result, a=a, b=b, op=op)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
