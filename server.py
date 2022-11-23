from flask import Flask, jsonify, request, make_response
from organization import Organizer
from game import Mafia

app = Flask(__name__)


def plug():
    """its plug"""
    pass


game_implementer = Mafia()
technical_implementer = Organizer()
tasks = {
    "GET": {
        "im new player": [
            technical_implementer.new_client,
            game_implementer.register_new
        ],
        "current situation": [
            technical_implementer.situation,
            game_implementer.situation
        ]
    },
    "DELETE": {
        "im leave": game_implementer.annul_client
    },
    "POST": {
        "im ready for game": game_implementer.ready
    },
    "PUT": {
        ""
    }
}


@app.route('/', methods=["GET", "POST", "PUT", "DELETE"])
def index():
    if not request.json or 'title' not in request.json:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    if request.method == "GET":
        tech = tasks[request.method][request.json["title"]][0]()
        game = tasks[request.method][request.json["title"]][1](tech, request.json)
        return jsonify({'error': "", 'tech': tech, 'game': game})
    elif request.method in ["DELETE", "POST"]:
        tasks[request.method][request.json["title"]](request.json)
        return jsonify({'error': ""})
    elif request.method == "PUT":
        return jsonify(tasks[request.method][request.json["title"]](request.json))


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
