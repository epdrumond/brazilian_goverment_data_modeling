import requests
import json
import pandas as pd
from os.path import join

class gov_data:

    def __init__(self):
        key_path = '/home/edilson/Desktop/chave_api_gov'
        self.api_key = {'chave-api-dados': open(key_path, 'r').read().strip('\n')}

    def get_url(self, request_type, **params):
        base_url = 'http://api.portaldatransparencia.gov.br/api-de-dados/'
        if (request_type == 'orgaos-siafi') or (request_type == 'orgaos-siape'):
            return base_url + request_type

    def get_data(self, request_type, request_subtype=None, **params):
        try:
            url = self.get_url(request_type, **params)
            request_data = requests.get(url, verify=True, headers=self.api_key).json()

            self.export_data(request_data, request_type)
        except Exception as e:
            print(e)

    def export_data(self, data, file_name, path=''):
        export_df = pd.DataFrame(data)
        export_df.to_csv(join(path, file_name), sep=';', index=False)
