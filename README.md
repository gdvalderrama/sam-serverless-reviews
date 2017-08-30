AWS SAM (serverless application model)

## AWS SAM Local

Use aws sam local to test and debug locally.

### Setup install

* install docker
* install aws sam local: `npm install -g aws-sam-local`
* install Go (v1.8+): `brew install go`
* set GO Env variables (see below)
* run `go get github.com/awslabs/aws-sam-local`

#### GO Env variables

`export GOROOT=/usr/local/opt/go/libexec`

`export GOPATH=$HOME/.go`

`export PATH=$PATH:$GOROOT/bin:$GOPATH/bin`

#### Set local DynamoDB

Follow instructions:
http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html

To use the AWS CLI with the local dynamoDB, simply add `--endpoint-url http://localhost:8000` to
each command

Example to create the table reviewTable:

```
aws dynamodb create-table --table-name reviewTable
--attribute-definitions AttributeName=id,AttributeType=S
--key-schema AttributeName=id,KeyType=HASH
--provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
--endpoint-url http://localhost:8000
```

### Use

* validate the template yaml: `sam validate`
* run API Gateway locally: `sam local start-api`
* invoke a lambda function: `sam local invoke "FunctionName" -e event.json`

Include environment variables:

* via external file: `sam local start-api --env-vars file_with_env_vars.json`
* via shell: `TABLE_NAME=reviewTable sam local start-api`

#### DynamoDB local

To run:
`java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb`

The DB must be running while testing functions that need to access it.

Acces the DynamoDB Javascript Shell on: `http://localhost:8000/shell/`

#### Environment variables

##### Via external JSON file
To correctly use defined environment variables use --env-vars argument on invoke or start-api to
provide a JSON file that contains values for environment variables defined in your function.

Example set review table name:

```
{
  "GetAllFunction": {
    "TABLE_NAME": "reviewTable",
  },
  "GetFunction": {
    "TABLE_NAME": "reviewTable",
  },
  "PutFunction": {
    "TABLE_NAME": "reviewTable",
  },
  "DeleteFunction": {
    "TABLE_NAME": "reviewTable",
  },
}
```

##### Via Shell

Simple define the variable while calling `sam`.

Example: `TABLE_NAME=reviewTable sam local start-api`

This way is simpler when the variable is used multiple times.
