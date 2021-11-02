FROM jupyterhub/jupyterhub:1.4.2

ENV TZ America/New_York

# User needs to be a part of the docker group in order to spawn notebook containers
RUN groupadd --gid 999 jupyterhub_user && \
    useradd --uid 4001 --gid 999 --shell /bin/bash --create-home jupyterhub_user && \
    chown -R 4001:999 /srv/

COPY --chown=4001:999 requirements.txt .
RUN pip install -r requirements.txt

USER jupyterhub_user

COPY jupyterhub_config.py .
