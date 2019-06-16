import os
from datetime import datetime as dt
import werkzeug
from flask_restful import reqparse

import requests
from flask import current_app, jsonify
from werkzeug.utils import secure_filename


class TransformType:

    date_string_format = "%m/%d/%Y"
    currency = {
        '₴': 'UAH',
        '$': 'USD',
        '€': 'EUR'
        }

    def transform_to_date(self, date_string):
        return self._validate_date(date_string)

    def transform_to_float(self, digit_string):
        return self._validate_digit_float(digit_string)

    def transform_to_int(self, digit_string):
        return self._validate_digit_int(digit_string)

    @staticmethod
    def transform_to_string(string):
        return str(string)

    def transform_to_currencies(self, currency_string):
        return self._validate_currency(currency_string)

    @staticmethod
    def _validate_digit_float(string_to_validate):
        try:
            return float(string_to_validate)
        except ValueError:
            raise ValueError("Please input only digit ot float like string")

    @staticmethod
    def _validate_digit_int(string_to_validate):
        try:
            return int(string_to_validate)
        except ValueError:
            raise ValueError("Please input only digit ot float like string")

    def _validate_date(self, date_string):
        try:
            return dt.strptime(date_string, self.date_string_format)
        except ValueError:
            raise ValueError("Please provide time in needed format: %d/%m/%Y")

    def _validate_currency(self, currency_string):
        length_of_digits = len(currency_string) - 1
        for key in self.currency.keys():
            if key in currency_string and self._validate_digit_float(
                    currency_string[:length_of_digits]):
                return {'currency_value': self._validate_digit_float(
                    currency_string[:length_of_digits]), 'currency':
                    self.currency[key]}
        raise ValueError(f'Please input file with correct currencies '
                         f'types: {self.currency.keys()} or values')


class RequestSender:

    session_service_url = ''
    project_service_url = ''

    def get_session(self):
        data = requests.get(self.session_service_url)
        return data

    def send_chunk(self, data):
        data_chunk = jsonify(data)
        return requests.post(self.project_service_url, {'data': data_chunk})

    def send_status(self, status):
        return requests.put(self.project_service_url, {'status': status})


def remove_file(filename):
    os.remove(filename)


def save_filename(file):
    filename = secure_filename(file.filename)
    return os.path.join(current_app.config['UPLOAD_FOLDER'], filename)


def post_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('file', type=werkzeug.FileStorage,
                        location='files')
    data = parser.parse_args()
    return data
