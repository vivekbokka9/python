import boto3
ecs = boto3.client('ecs')

def lamba_handler(event, context):


response = ecs.update_service(
    cluster='vivek-cluster',
    service='vivek-service',
    taskDefinition='vivek-task',
    forceNewDeployment=True,
)

print(response)