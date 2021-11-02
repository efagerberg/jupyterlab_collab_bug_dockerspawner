import os
import sys


# Notebook spawning
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
c.DockerSpawner.image = os.environ["DOCKER_JUPYTER_IMAGE"]
c.DockerSpawner.network_name = os.environ["DOCKER_NETWORK_NAME"]
# Explicitly set notebook directory because we'll be mounting a host volume to
# it.  Most jupyter/docker-stacks *-notebook images run the Notebook server as
# user `jovyan`, and set the notebook directory to `/home/jovyan/work`.
# We follow the same convention.
notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR", "/home/jovyan/work")
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {
    # Persist user work
    "{username}-jupyter-workspace": {"bind": notebook_dir, "mode": "rw"},
    # Have a shared docker data volume
    "shared-jupyter-workspace": {
        "bind": os.path.join(notebook_dir, "shared"),
        "mode": "rw",
    },
}
# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = "0.0.0.0"
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = "jupyterhub"
# Make jupyterlab collaborative
c.Spawner.cmd = ["jupyter-labhub", "--collaborative"]

# Authentication
c.JupyterHub.authenticator_class = "jupyterhub.auth.DummyAuthenticator"
