FROM python:3.11
WORKDIR /app
WORKDIR /app/static
WORKDIR /app/madia

RUN pip3 install --upgrade pip wheel
RUN python -m pip install Pillow

ENV PYTHONUNBUFFERED=1

ADD requirements.txt .
RUN pip3 --no-cache-dir install -r requirements.txt

RUN rm -rf ~/.cache/pip
COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]