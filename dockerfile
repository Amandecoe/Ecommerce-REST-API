FROM python:3.13-slim 
#image extended by us, provided from python

ENV PYTHONDONTWRITEBYTECODE=1 \ 
#It is not going to write the byte code files into the docker container
PYTHONUNBUFFERED=1 
#prevents python from buffering output, allows log messages into dump messages and not buffered

WORKDIR /app 
#sets the working directory
RUN apt-get install -y curl
#install system dependent packages

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
#installs uv
#uv provides both distroless Docker images, which are useful for copying uv binaries into your own image builds, and images derived from popular base images, which are useful for using uv in a container.

COPY EcommerceApi/requirements.txt .
RUN uv pip install -r requirements.txt --system
#installs the requirements file

COPY EcommerceApi/ .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#command to run the django server