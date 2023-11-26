import requests
import os


class Authorization:
    token = ''
    headers = {}

    def __init__(self):
        self.set_headers()

    def set_headers(self):
        access_token = os.environ['ACCESS_TOKEN']
        self.headers = {
            'Authorization': f'Bearer {access_token}'
        }

    def get_headers(self):
        return self.headers

    @staticmethod
    def get_token():
        data = {
            'client_id': os.environ['CLIENT_ID'],
            'client_secret': os.environ['CLIENT_SECRET'],
            'code': os.environ['AUTHORIZATION_CODE'],
            'grant_type': 'authorization_code'
        }

        try:
            response = requests.post('https://www.strava.com/oauth/token', data=data).json()
            access_token = response.get('access_token')
            if access_token:
                return access_token
        except Exception as e:
            print(f"Erro na solicitação {e}")
        return None
