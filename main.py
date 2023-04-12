import boto3
import json
sqs=boto3.resource('sqs')
queue=sqs.create_queue(
 QueueName='my_queue'
 
 )
print("Created queue '%s' with URL=%s",'queues',queue.url)

def send_message(queue_url):
    sqs_client = boto3.client("sqs")

    message = {}
    response = sqs_client.send_message(
        QueueUrl=f"https://sqs.us-east-2.amazonaws.com/873122993178/first",
        MessageBody=json.dumps(message)
    )
    print(response)