from flask import Flask, jsonify, request

calcAPI = Flask(__name__)


@calcAPI.route('/rut', methods=['POST'])
def root_of():
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
        return result


@calcAPI.route('/expo', methods=['POST'])
def expo():
        data = request.get_json()
        ip1 = data["input_1"]
        ip2 = data["input_2"]
        res = ip1 ** ip2
        result = {f"The value of {ip1} to the power {ip2} is": res}
        return result


@calcAPI.route('/log', methods=['POST'])
def log():
        data = request.get_json()
        ip1 = data["input_1"]
        ip2 = data["input_2"]
        n = 1000000000.0
        ln_ip1 = n * ((ip1 ** (1 / n)) - 1)
        ln_ip2 = n * ((ip2 ** (1 / n)) - 1)
        res = ln_ip1 / ln_ip2
        result = {f"The value of log {ip1} to the base {ip2} is": res}
        return result


if __name__ == '__main__':
    calcAPI.run(debug=True)
