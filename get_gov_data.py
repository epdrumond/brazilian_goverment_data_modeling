#Import libraries
import pandas as pd
import requests
import json

from gov_data_class import gov_data

#Get key for API connection
key_path = '/home/edilson/Desktop/chave_api_gov'
api_key = {'chave-api-dados': open(key_path, 'r').read().strip('\n')}

#Test request
gov = gov_data()

gov.get_data(request_type='orgaos-siafi')
