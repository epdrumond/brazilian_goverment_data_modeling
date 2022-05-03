#Import libraries
import pandas as pd
import requests
import json

from gov_data_class import gov_data

#Get key for API connection
key_path = '/home/edilson/Desktop/chave_api_gov'
api_key = {'chave-api-dados': open(key_path, 'r').read().strip('\n')}

#Instance class
gov = gov_data()

#Query the federal government budget
params = {'year': 2020, 'mode': 'complete'}
gov.get_data(request_type='plano-orcamentario', **params)

#Get the names and codes for all federal organs
#gov.get_data(request_type='orgaos-siafi')
#gov.get_data(request_type='orgaos-siape')

#params = {
#    'emission_date': '27/01/2022',
#    'fase': 1,
#    'managing_organ': '02002',
#    'page': 1
#}

#gov.get_data(
#    request_type='despesas',
#    request_subtype='documentos',
#    params=params
#)
