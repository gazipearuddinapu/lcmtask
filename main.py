from flask import Flask, request
import math

app = Flask(__name__)

@app.route('/s1810128148_ru_ac_bd')
def get_lcm():
    # URL থেকে x এবং y এর মান নেয়া
    x_val = request.args.get('x')
    y_val = request.args.get('y')

    try:
        # ইনপুট সংখ্যা না হলে বা খালি থাকলে ValueError হবে
        x = int(x_val)
        y = int(y_val)

        # স্বাভাবিক সংখ্যা (natural numbers) বা নন-নেগেটিভ চেক
        if x < 0 or y < 0:
            return "NaN"

        # লসাগু (LCM) নির্ণয়
        if x == 0 or y == 0:
            result = 0
        else:
            result = abs(x * y) // math.gcd(x, y)
        
        return str(result)

    except (TypeError, ValueError):
        return "NaN"
