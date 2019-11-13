Blog post: https://serverless.com/blog/serverless-python-packaging/

# Create a new function with boilerplate code
```bash
serverless create \
  --template aws-python3 \
  --name test-function \
  --path test-function
```

# Create a new virtual environment for dependencies
```
virtualenv venv --python=python3
source venv/bin/activate
```

# Save depdendencies
```
pip freeze > requirements.txt
```

# Node tool for packaging dependencies (using Docker)
```
npm init
npm install --save serverless-python-requirements
```

Include the following:
```yaml
# serverless.yml

plugins:
  - serverless-python-requirements

custom:
  pythonRequirements:
    dockerizePip: non-linux
```

# Run
```
# Upload
sls deploy

# Invoke function
sls invoke -f hello
```

# Cleanup
Exit the virtual environment



