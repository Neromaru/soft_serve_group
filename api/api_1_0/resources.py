from flask import jsonify
from flask_restful import Resource, reqparse
import werkzeug
import pandas as pd


class UploadCsv(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=werkzeug.FileStorage,
                            location='files')
        data = parser.parse_args()
        file = data['file']
        self._form_request_data(file)
        return jsonify(dict(hi=True))

    def _form_request_data(self, file):
        for chunk in pd.read_csv(file, chunksize=50, sep=','):
            headers = list(chunk)
            values = chunk.values
            form_data = dict(headers=headers, values=values)
            self._send_request(form_data)

    def _send_request(self, data):
        pass
