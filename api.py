import chess
from flask import Flask, request, jsonify, render_template
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def list_available_moves(chess_figure, current_field):
    if request.method == "GET":
        if chess_figure == "king":
            k = chess.King(current_field[0], int(current_field[1:]))
            available_moves_list = k.list_available_moves()

            if type(available_moves_list) is tuple:
                return jsonify(
                    {
                        "availableMoves": available_moves_list[0],
                        "error": available_moves_list[1],
                        "figure": chess_figure,
                        "currentField": current_field,
                    }
                )
            else:
                return jsonify(
                    {
                        "availableMoves": available_moves_list,
                        "error": None,
                        "figure": chess_figure,
                        "currentField": current_field,
                    }
                )


@app.errorhandler(404)
def invalid_route(e):
    return jsonify({"responseCode": 404, "message": "Route not found"})


@app.errorhandler(500)
def invalid_route(e):
    return jsonify({"responseCode": 500, "message": "Server error"})


if __name__ == "__main__":
    app.run(debug=False)
