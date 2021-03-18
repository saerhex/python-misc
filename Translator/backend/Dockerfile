FROM python:3.9
WORKDIR /src
COPY ./requirements.txt /src
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["./run.py"]