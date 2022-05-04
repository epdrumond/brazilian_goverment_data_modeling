#Import libraries
import pandas as pd
import requests
import json
from tqdm import tqdm

from gov_data_class import gov_data

#Get key for API connection
key_path = '/home/edilson/Desktop/chave_api_gov'
api_key = {'chave-api-dados': open(key_path, 'r').read().strip('\n')}

#Instance class
gov = gov_data()

#Extract data ------------------------------------------------------------------

#1. List of organs
params = {'mode': 'complete'}
gov.get_data(request_type='orgaos-siafi', **params)
print('Orgãos SIAFI')
gov.get_data(request_type='orgaos-siape', **params)
print('Orgãos SIAPE')

#2. Federal government budget from 2018 to 2022
for year in tqdm(range(2018, 2023)):
    params = {
        'year': year,
        'mode': 'complete',
        'export_file': f'plano_orcamentario_{year}.txt'
    }
    gov.get_data(request_type='plano-orcamentario', **params)

print('Planos orçamentários')
