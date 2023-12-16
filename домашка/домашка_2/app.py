from flask import Flask, request, jsonify
from calculator import Lexer, RPNConverter, Calculator

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression')

    if expression is None:
        return jsonify({'error': 'No expression provided'}), 400

    try:
        # Лексический анализ и преобразование в RPN
        lexer = Lexer()
        rpn_converter = RPNConverter()
        calculator = Calculator()

        tokens = lexer.tokenize(expression)
        rpn_expression = rpn_converter.to_rpn(tokens)
        result = calculator.calculate(rpn_expression)

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
