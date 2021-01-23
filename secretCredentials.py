#Archivo para almacenar nuestras credenciales secretas, IDs, URIs, etc.

import requests

Client_ID = '*******************************'
Client_Secret = '******************************'

User_ID = '*************'
OnRepeat_ID = '******************'

Song_ID = '1XylkHvQL5p3w8f7yuDgxu'

auth_url = 'https://accounts.spotify.com/api/token'

baseurl = 'https://api.spotify.com/v1/'

def GetAccessToken():
    auth_resp = requests.post(auth_url, {'grant_type': 'client_credentials',
                                         #'scope': 'user-read-recently-played',
                                         #'scope': ['ugc-image-upload',
                                         #          'playlist-modify-private',
                                         #          'user-library-read',
                                         #          'user-read-recently-played',
                                         #          'user-top-read',
                                         #          'playlist-modify-public',
                                         #          'playlist-read-private'],
                                         'scope': 'ugc-image-upload playlist-modify-private user-library-read'\
                                                  'user-read-recently-played user-top-read playlist-modify-public'\
                                                  'playlist-read-private',
                                         'redirect_uri': 'http://127.0.0.1:5000/spotify/callback',
                                         #'redirect_uri': 'http://localhost:8888/callback',
                                         'show_dialog': True,
                                         'client_id': Client_ID,
                                         'client_secret': Client_Secret })

    # respuesta a JSON
    auth_data = auth_resp.json()

    # guardar el access token
    atoken = auth_data['access_token']

    return atoken

access_token = 'BQBtaqGX816X75pQzMqU_4OPQ68JrV-qCNT5f5lKRuRROyJQbS4P3nxJ8mRiQbxd2eV2fDHaMpc3LS5vkO3XNx4dlAon5XPyGhZCrmA7effmSGUmgxJvg6uYFjcZ5swfLYbbaJ-NbiYhwheMRprLK8kb-dnw0EMsfE3_nnWGpNLxWmwxojmcAEeNfx5mB-R1MaabOJUuQx2yA1oRK-_j7azI9O7zQVrtsWMaP6zCLro29I3v4HjZXiaZh12Q763dcdDSn8lCAq4l-fKrjKli3ZE'
#access_token2 = 'BQAXBcTT9IVRVcYeKgnf_nOSkukNj9EhpYGN5poKHnojunrLnYVsOoAEzqvW8IpRzzqs4GUktIB-z_dY9TPrgskPhbSL6bJcD_KwanMPXbMVS9M8g-0QXTgQUULbm8DzJBcWf0bUnZFzqQ-L_O6SYvLHyA-j5FPu'
