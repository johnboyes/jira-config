
# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT=3
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

COPY .devcontainer/scripts/* /tmp/scripts/

USER root

RUN /tmp/scripts/install-hadolint.sh \
    && /tmp/scripts/install-gauge.sh \
    && rm -rf /tmp/scripts

USER vscode
