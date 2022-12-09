FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore
WORKDIR /code
RUN apt-get update && apt-get install -y wkhtmltopdf
RUN pip install --upgrade pip
RUN pip install pandas
RUN pip install --upgrade setuptools pip
RUN pip install opencv-python
RUN pip install --upgrade pip
RUN pip install --upgrade Pillow
RUN pip install PyPDF2
RUN pip install pdfkit

COPY 2022-2-Squad08/main.py .
CMD ["python3", "main.py"]