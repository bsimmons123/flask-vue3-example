from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='./dist', static_url_path='')


# Catch all route
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def catch_all(path):
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()
