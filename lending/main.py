# from flask import Flask
# from flask import render_template


# app = Flask(__name__, static_url_path='')
# # app = Flask(__name__, template_folder='web')

# import os


# print(os.path.realpath(__file__))
# @app.route('/')
# def hello():
#     print('************************' * 50)
#     print(os.path.realpath(__file__))

#     # return 'render_template('index.html')'

#     return render_template('index.html')


import tornado.web
import tornado.ioloop
import os
import json


class DataForm(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html')


class DataResponse(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "content-type")
        self.set_header(
            'Access-Control-Allow-Methods',
            'POST, GET, OPTIONS, PATCH, PUT'
        )

    def post(self):
        owner_name = self.get_body_argument('owner_name')
        owner_email = self.get_body_argument('owner_email')
        tax_id = self.get_body_argument('tax_id')
        business_name = self.get_body_argument('business_name')
        requested_amount = self.get_body_argument('requested_amount')
        security_number = self.get_body_argument('security_number')

        requested_amount = int(requested_amount)

        lending_response = 'Approved'
        if requested_amount > 500000:
            lending_response = 'Declined'
        elif requested_amount == 500000:
            lending_response = 'Undecided'

        self.write({
            'Response': lending_response,
            'Owner name': owner_name,
            'Owner email': owner_email,
            'Tax id': tax_id,
            'Business name': business_name,
            'Requested amount': requested_amount,
            'Security number': security_number,
        })


class DataShowResponse(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/result.html')


def main():
    app = tornado.web.Application(
        [
            (r'/', DataForm),
            (r'/response/', DataResponse),
            (r'/response-show/', DataShowResponse),
        ],
        static_path=os.path.join(os.path.dirname(__file__), 'static')
    )

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
