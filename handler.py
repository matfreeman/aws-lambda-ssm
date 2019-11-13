import os, time, json, traceback, configparser
import boto3
from aws_xray_sdk.core import patch_all

# Enable x-ray tracing
patch_all()

# Client for SSM
client = boto3.client('ssm')

# Environment variables
environment = os.environ["ENVIRONMENT"]
db_parameters_path = os.environ["DB_PARAMETERS_PATH"]
param_store_path = "/{}/".format(environment)

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
    return str(params.get(db_parameters_path, 'table_name'))

def lambda_handler(event, context):
    result = load_ssm_paramters(param_store_path)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! Result from ' +  param_store_path + ' is: ' + result)
    }
