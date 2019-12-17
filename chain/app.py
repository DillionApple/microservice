import random
import sys

from flask import Flask

app = Flask(__name__)

@app.route('/random_str/')
def random_str():
    s = [chr(random.randint(ord('A'), ord('Z'))) for _ in range(1024)]
    s = "".join(s)

    return s

if __name__ == "__main__":
    PORT = sys.argv[1]
    app.run(host="0.0.0.0", port=PORT)
