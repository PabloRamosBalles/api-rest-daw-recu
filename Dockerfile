FROM python:3.10-alpine

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_HOST='0.0.0.0'

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN python -m virtualenv virtualen
RUN source venv/bin/activate
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run", "--debug"]