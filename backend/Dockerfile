# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/backend/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/backend/requirements.txt

# 
COPY .   /code/backend