FROM python:3.12
WORKDIR /PycharmProjects
COPY . .
CMD ["python", "main.py"]