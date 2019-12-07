from flask import Flask,jsonify
from flask_restplus import Resource, Api

from faker import Faker

app = Flask(__name__)
api = Api(app, version='0.1.0', title='Faker', description="""## Faker API
**당신의 새로운 영웅을 소환하세요.**
""")
ns = api.namespace('Hero', description='영웅이 여기 잠들다.')
fake = Faker("ko-KR")

@ns.route('/new_hero')
class NewHero(Resource):
    def get(self):
        '''새 영웅 프로필을 생성합니다.'''
        profile = fake.profile()
        profile.pop('current_location')
        profile['phone_number'] = fake.phone_number()
        return jsonify(profile)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
