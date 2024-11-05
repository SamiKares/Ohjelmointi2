from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku')
def is_prime_number():
    args = request.args
    luku1 = int(args.get("luku1"))
    isprime = "True"
    if luku1 <= 1:
        isprime = "False"
    for i in range(2, int(luku1)):
        if luku1 % i == 0:
            isprime = "False"
    vastaus = {
        "Numero": luku1,
        "isPrime": isprime
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)