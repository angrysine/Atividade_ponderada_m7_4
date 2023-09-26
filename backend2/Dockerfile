# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt
COPY ./requirements2.txt /code/requirements2.txt
COPY ./teste_api.pkl /code/teste_api.pkl
COPY ./archive/Mall_Customers.csv /code/archive/Mall_Customers.csv
RUN mkdir ./images
# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements2.txt

# 
COPY ./app.py /code/app.py

# 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]