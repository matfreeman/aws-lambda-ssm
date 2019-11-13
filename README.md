# aws-lambda-ssm
A lambda function that uses x-ray to report on AWS Systems Manager Parameter Store retrieval times

## Prerequisites

* Configure AWS credentials: `aws configure`
* NPM dependencies installed: `npm install serverless-python-requirements`
* Requires Serverless: https://www.npmjs.com/package/serverless
* Requires a role AWS execution role for the lambda function (with appropriate permissions) and parameters defined
* TODO: add execution role & parameter store key-values to the codebase

## Use
Deploy the function
```
npm install
sls deploy

# Invoke function
sls invoke -f hello --log
```

## Useful commands
```
# Setup virtual environment
virtualenv venv --python=python3
source venv/bin/activate

# Save depdendencies
pip freeze > requirements.txt

# Node tool for packaging dependencies (using Docker)
npm init
npm install --save serverless-python-requirements

# Exit virtual environment
deactivate
```

# References
* Serverless python packaging: https://serverless.com/blog/serverless-python-packaging/
* Virtual environments: https://sourabhbajaj.com/mac-setup/Python/virtualenv.html
* Using AWS with Systems Manager Parameter Store: https://aws.amazon.com/blogs/compute/sharing-secrets-with-aws-lambda-using-aws-systems-manager-parameter-store/