
from flask import Flask
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)

#app.config.SWAGGER_UI_OAUTH_CLIENT_ID = 'MyClientId'
#app.config.SWAGGER_UI_OAUTH_REALM = '-'
app.config.SWAGGER_UI_OAUTH_APP_NAME = 'Operation'

api = Api(
    app, 
    prefix='/api',
    doc='/doc',
    title=app.config.SWAGGER_UI_OAUTH_APP_NAME,
 #   security={'OAuth2': ['read', 'write']},
 #   authorizations={
 #       'OAuth2': {
 #           'type': 'oauth2',
 #           'flow': 'implicit',
 #           'authorizationUrl': 'https://idp.example.com/authorize?audience=https://app.example.com',
 #           'clientId': app.config.SWAGGER_UI_OAUTH_CLIENT_ID,
 #           'scopes': {
 #               'openid': 'Get ID token',
 #               'profile': 'Get identity',
 #           }
 #       }
 #   }
)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/mul', endpoint='mul')
@api.param('a', "First value")
@api.param('b', "Second value")
class Square(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('a', type=int, help='Value a cannot be converted')
        parser.add_argument('b', type=int, help='Value b cannot be converted')
        args = parser.parse_args()
        #s = 0;
        #for key, value in args:
        s = (int(args['a']) * int(args['b']))
        return {'ans' : s}

@api.route('/sum', endpoint='sum')
@api.param('a', "First value")
@api.param('b', "Second value")
class Sum(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('a', type=int, help='Value a cannot be converted')
        parser.add_argument('b', type=int, help='Value b cannot be converted')
        args = parser.parse_args()
        #s = 0;
        #for key, value in args:
        s = (int(args['a']) + int(args['b']))
        return {'ans' : s}

@api.route('/sub', endpoint='sub')
@api.param('a', "First value")
@api.param('b', "Second value")
class Sub(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('a', type=int, help='Value a cannot be converted')
        parser.add_argument('b', type=int, help='Value b cannot be converted')
        args = parser.parse_args()
        #s = 0;
        #for key, value in args:
        s = (int(args['a']) - int(args['b']))
        return {'ans' : s}                 

if __name__ == '__main__':
    app.run(debug=True)     
 
