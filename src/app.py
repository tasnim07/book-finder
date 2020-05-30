from flask import Flask, jsonify, request
from book_finder import index, search


app = Flask(__name__)


@app.route('/search', methods=['POST'])
def get_search():
    body = request.json

    if 'queries' not in body or not isinstance(body['queries'], list):
        return jsonify(
            {'error': 'queries field must be passed/queries must be a list'}
        ), 400

    return jsonify(search.get_api_search_result(body)), 200


if __name__ == '__main__':
    # first step is to index data.
    index.index_book_data()

    app.run(debug=True)
