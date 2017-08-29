import os
import logging
import json
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb_client = boto3.client("dynamodb")
table_name = os.environ["TABLE_NAME"]

logger.info("Using table {}".format(table_name))


def create_response(status_code, body):
    response = {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body) or ""
    }
    logger.info("Created response: {}".format(response))
    return response


def handler_get(event, context):
    logger.info("Received event {}".format(event))

    try:
        result = dynamodb_client.get_item(
            TableName=table_name,
            Key={"id": {"S": event["pathParameters"]["reviewId"]}}
        )
        logger.info("Get Item result: {}".format(result))
        return create_response(200, result["Item"])
    except ClientError as e:
        logger.info("Get Item failed: {}".format(e))
        return create_response(500, e.response["Error"]["Message"])


def handler_put(event, context):
    logger.info("Received event {}".format(event))
    item = json.loads(event["body"])['item']

    try:
        result = dynamodb_client.put_item(
            TableName=table_name,
            Item=item
        )
        logger.info("Get Item result: {}".format(result))
        return create_response(200, result)
    except ClientError as e:
        logger.info("Get Item failed: {}".format(e))
        return create_response(500, e.response["Error"]["Message"])


def handler_delete(event, context):
    logger.info("Received event {}".format(event))

    try:
        result = dynamodb_client.delete_item(
            TableName=table_name,
            Key={"id": {"S": event["pathParameters"]["reviewId"]}}
        )
        logger.info("Delete Item result: {}".format(result))
        return create_response(200, result)
    except ClientError as e:
        logger.info("Delete Item failed: {}".format(e))
        return create_response(500, e.response["Error"]["Message"])
