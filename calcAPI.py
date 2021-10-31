from flask import Flask, jsonify, request

calc_2_backend = Flask(__name__)


@calc_2_backend.route('/root', methods=['GET', 'POST'])
def root_of():
    if request.method == 'GET':
        ip1 = 9
        ip2 = 2
        res = ip1 ** (1 / ip2)
        if ip2 == 2:
            op = f"The value of square root of {ip1} is"
        elif ip2 == 3:
            op = f"The value of cube root of {ip1} is"
        else:
            op = f"The value of {ip2} root of {ip1} is"
        result = {op: res}
        return result, HTTPStatus.CREATED
    elif request.method == 'POST':
        data = request.get_json()
        ip1 = data["input_1"]
        ip2 = data["input_2"]

        res = ip1 ** (1 / ip2)
        if ip2 == 2:
            op = f"The value of square root of {ip1} is"
        elif ip2 == 3:
            op = f"The value of cube root of {ip1} is"
        else:
            op = f"The value of {ip2} root of {ip1} is"
        result = {op: res}
        return result, HTTPStatus.CREATED


@calc_2_backend.route('/exponential', methods=['GET', 'POST'])
def expo():
    if request.method == 'GET':
        ip1 = 10
        ip2 = 4
        res = ip1 ** ip2
        result = {f"The value of {ip1} to the power {ip2} is": res}
        return result, HTTPStatus.CREATED
    elif request.method == 'POST':
        data = request.get_json()
        ip1 = data["input_1"]
        ip2 = data["input_2"]
        res = ip1 ** ip2
        result = {f"The value of {ip1} to the power {ip2} is": res}
        return result, HTTPStatus.CREATED


@calc_2_backend.route('/logarithm', methods=['GET', 'POST'])
def log():
    if request.method == 'GET':
        ip1 = 10
        ip2 = 4
        n = 1000000000.0
        ln_ip1 = n * ((ip1 ** (1 / n)) - 1)
        ln_ip2 = n * ((ip2 ** (1 / n)) - 1)
        res = ln_ip1 / ln_ip2
        result = {f"The value of log {ip1} to the base {ip2} is": res}
        return result, HTTPStatus.CREATED
    elif request.method == 'POST':
        data = request.get_json()
        ip1 = data["input_1"]
        ip2 = data["input_2"]
        n = 1000000000.0
        ln_ip1 = n * ((ip1 ** (1 / n)) - 1)
        ln_ip2 = n * ((ip2 ** (1 / n)) - 1)
        res = ln_ip1 / ln_ip2
        result = {f"The value of log {ip1} to the base {ip2} is": res}
        return result, HTTPStatus.CREATED


@calc_2_backend.route('/function/<string:op>', methods=['POST'])
def math_op(op):
    if op == "root":
        data = request.get_json()
        ip1 = data["input_1"]
        ip2 = data["input_2"]
        res = ip1 ** (1 / ip2)
        if ip2 == 2:
            op = f"The value of square root of {ip1} is"
        elif ip2 == 3:
            op = f"The value of cube root of {ip1} is"
        else:
            op = f"The value of {ip2} root of {ip1} is"
        result = {op: res}
        return jsonify(result), HTTPStatus.CREATED
    elif op == "exponential":
        data = request.get_json()
        ip1 = data["input_1"]
        ip2 = data["input_2"]
        res = ip1 ** ip2
        result = {f"The value of {ip1} to the power {ip2} is": res}
        return jsonify(result), HTTPStatus.CREATED
    elif op == "logarithm":
        data = request.get_json()
        ip1 = data["input_1"]
        ip2 = data["input_2"]
        n = 1000000000.0
        ln_ip1 = n * ((ip1 ** (1 / n)) - 1)
        ln_ip2 = n * ((ip2 ** (1 / n)) - 1)
        res = ln_ip1 / ln_ip2
        result = {f"The value of log {ip1} to the base {ip2} is": res}
        return jsonify(result), HTTPStatus.CREATED


@calc_2_backend.route('/function', methods=['POST'])
def combined_op():
    data = request.get_json()
    ip1 = data["input_1"]
    ip2 = data['input_2']
    res1 = ip1 ** (1 / ip2)
    if ip2 == 2:
        op1 = f"The value of square root of {ip1} is"
    elif ip2 == 3:
        op1 = f"The value of cube root of {ip1} is"
    else:
        op1 = f"The value of {ip2} root of {ip1} is"

    res2 = ip1 ** ip2
    op2 = f"The value of {ip1} to the power {ip2} is"
    n = 1000000000.0
    ln_ip1 = n * ((ip1 ** (1 / n)) - 1)
    ln_ip2 = n * ((ip2 ** (1 / n)) - 1)
    res3 = ln_ip1 / ln_ip2
    op3 = f"The value of log {ip1} to the base {ip2} is"
    result = [{op1: res1}, {op2: res2}, {op3: res3}]
    return jsonify(result)


if __name__ == '__main__':
    calc_2_backend.run(debug=True)
