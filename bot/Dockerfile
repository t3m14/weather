# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/bot/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/bot/requirements.txt

# 
COPY .   /code/bot/

CMD ["python", "/code/bot/main.py"]