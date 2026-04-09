from flask import Flask, request
import math

app = Flask(__name__)
@app.route('/s1810128148_ru_ac_bd')
def get_lcm():
    x_val = request.args.get('x')
    y_val = request.args.get('y')

    try:
        x = int(x_val)
        y = int(y_val)

        if x < 0 or y < 0:
            return "NaN"

        if x == 0 or y == 0:
            result = 0
        else:
            result = abs(x * y) // math.gcd(x, y)
        
        return str(result)

    except (TypeError, ValueError):
                return "NaN"

if __name__ == "__main__": app.run()