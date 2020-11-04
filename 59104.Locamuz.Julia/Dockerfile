FROM python:3

RUN git clone https://github.com/jlocamuz/tateti.git

RUN pip install parameterized

WORKDIR /tateti

CMD ["python3","-m" ,"unittest"]

