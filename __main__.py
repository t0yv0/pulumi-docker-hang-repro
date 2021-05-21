import base64
import pulumi
import pulumi_aws as aws
import pulumi_docker as docker
from pulumi_aws import ecr

def get_registry_info(rid):
    creds = aws.ecr.get_credentials(rid)
    decoded = base64.b64decode(creds.authorization_token).decode()
    parts = decoded.split(':')
    if len(parts) != 2:
        raise Exception("Invalid credentials")
    return docker.ImageRegistry(creds.proxy_endpoint, parts[0], parts[1])


repository = ecr.Repository("test-repository", name="test-repository")
registry = repository.registry_id.apply(get_registry_info)


image = docker.Image(
    'my-image',
    build=docker.DockerBuild(context='.', args={}),
    image_name=repository.repository_url.apply(lambda url: url + ':latest'),
    registry=registry)
