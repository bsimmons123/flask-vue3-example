from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder='./dist', static_url_path='')

count = 0

# Catch all route
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def catch_all(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/count', methods=['POST'])
def api_count():
    global count
    count += 1
    return jsonify(count=count)


if __name__ == '__main__':
    app.run()
