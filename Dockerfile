FROM python:3.8

WORKDIR /app

COPY . .

ENV PYTHONUNBUFFERED=1

# # Install system dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     # tzdata \
#     python3-setuptools \
#     python3-pip \
#     python3-dev \
#     python3-venv \
#     git \
#     && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# # # install environment dependencies
# RUN pip3 install --upgrade pip 

# Install project dependencies
RUN pip install -r requirements.txt