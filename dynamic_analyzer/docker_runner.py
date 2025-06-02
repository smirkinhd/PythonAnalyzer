import docker

def run_container(image="nginx:alpine", port=8080):
    client = docker.from_env()
    container = client.containers.run(
        image,
        ports={"80/tcp": port},
        detach=True
    )
    return container
