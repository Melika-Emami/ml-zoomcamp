FROM python:3.12-slim

WORKDIR /app

RUN python -m pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY predict.py ./
COPY models/model_C=1.0.bin ./models/

EXPOSE 9696

ENTRYPOINT [ "waitress-serve", "--host=0.0.0.0", "--port=9696", "predict:app" ]

# Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging

# ENV PYTHONUNBUFFERED=1

# # Install pip requirements

# # COPY requirements.txt .
# # RUN python -m pip install -r requirements.txt

# RUN pip install pipenv

# COPY ["Pipfile", "Pipfile.lock"] .

# WORKDIR /app
# COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python", "05-deployment\predict.py"]
