import boto3
import json
client = boto3.client('secretsmanager')


def deleteSecret():
    response = client.delete_secret(
    SecretId='DatabaseProdSecrets',
    RecoveryWindowInDays=10,
    ForceDeleteWithoutRecovery=False
    )
    return response

deleteresp =deleteSecret()
print(deleteresp)