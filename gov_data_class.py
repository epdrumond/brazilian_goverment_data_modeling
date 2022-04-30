import requests
import json
import pandas as pd
from os.path import join

class gov_data:

    def __init__(self):
        key_path = '/home/edilson/Desktop/chave_api_gov'
        self.api_key = {'chave-api-dados': open(key_path, 'r').read().strip('\n')}

    def get_url(self, params):
        base_url = 'http://api.portaldatransparencia.gov.br/api-de-dados/'

        if (self.request_type == 'orgaos-siafi') or (self.request_type == 'orgaos-siape'):
            url = self.request_type
            export_file_name = self.request_type

        elif self.request_type == 'despesas':
            if self.request_subtype == 'documentos':
                date_url = f"?dataEmissao={params['emission_date']}"
                fase_url = f"&fase={params['fase']}"
                managing_organ_url = (
                    f"&gestao={params['managing_organ']}"
                    if 'managing_organ' in params.keys()
                    else ''
                )
                page_url = f"&pagina={params['page']}"
                managing_unit_url = (
                    f"&gestao={params['managing_unit']}"
                    if 'managing_unit' in params.keys()
                    else ''
                )

                url = \
                    f'{self.request_type}/{self.request_subtype}' + \
                    date_url + \
                    fase_url + \
                    managing_organ_url + \
                    page_url + \
                    managing_unit_url

                export_file_name = '{}_{}_{}_{}_{}'.format(
                    self.request_type,
                    self.request_subtype,
                    params['emission_date'].replace('/', '-'),
                    params['fase'],
                    params['page']
                )


        return base_url + url, export_file_name

    def get_data(self, request_type, request_subtype=None, **params):
        self.request_type = request_type
        self.request_subtype = request_subtype
        params = params['params']

        try:
            url, export_file = self.get_url(params)
            request_data = requests.get(url, verify=True, headers=self.api_key).json()

            self.export_data(request_data, export_file)
        except Exception as e:
            print(e)

    def export_data(self, data, file_name, path=''):
        export_df = pd.DataFrame(data)
        export_df.to_csv(join(path, file_name), sep=';', index=False)
