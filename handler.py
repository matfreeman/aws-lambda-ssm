import json
import time
import os
import boto3
import configparser
import traceback
from aws_xray_sdk.core import patch_all
patch_all()

client = boto3.client('ssm')

ENVIRONMENT = os.environ["ENVIRONMENT"]
DB_PARAMETERS_PATH = os.environ["DB_PARAMETERS_PATH"]
PARAM_STORE_PATH = "/{}/".format(ENVIRONMENT)

def test_function():
    time.sleep(1)

def process_params(params_list):
    config = configparser.ConfigParser()
    if 'Parameters' in params_list and len(params_list.get('Parameters')) > 0:
        for param in params_list.get('Parameters'):
            param_path = param.get('Name').split("/")
            param_name = param_path[len(param_path)-1]
            param_value = json.loads(param.get('Value'))
            param_dict = { param_name: param_value }
            config.read_dict(param_dict)
    return config

def load_ssm_paramters(param_path):
    params_list = client.get_parameters_by_path(
        Path=param_path,
        Recursive=False,
        WithDecryption=False
        )
    params = process_params(params_list)
    return str(params.get(DB_PARAMETERS_PATH, 'table_name'))

def lambda_handler(event, context):
    result = load_ssm_paramters(PARAM_STORE_PATH)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! Result from ' +  PARAM_STORE_PATH + ' is: ' + result)
    }
