FROM python:3.13-slim 
#image extended by us, provided from python

ENV PYTHONDONTWRITEBYTECODE=1 \ 
#It is not going to write the byte code files into the docker container
PYTHONUNBUFFERED=1 
#prevents python from buffering output, allows log messages into dump messages and not buffered

WORKDIR /app 
#sets the working directory
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
#installs uv
#uv provides both distroless Docker images, which are useful for copying uv binaries into your own image builds, and images derived from popular base images, which are useful for using uv in a container.

COPY EcommerceApi/requirements.txt .
