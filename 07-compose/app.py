from flask import Flask, request, jsonify
app = Flask(__name__)

def get_file_text():
    try:
        with open('file.txt') as f:
            txt = f.read()
        return txt
    except Exception as e:
        print(f'Exception occurs: {e}')
        return 'Hello World'

@app.route('/')
def hello_world():
    msg = get_file_text()
    return msg

@app.route('/query')
def query():
    print(request.args)
    name = request.args.get('name', 'no_input_name')
    return 'Your input is: {}'.format(name)

@app.route('/getjson')
def getjson():
    result = {'status': 'ok', 'result': 'result message'}
    return jsonify(result)

# flask run --port=8888

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
    

