FROM python
RUN pip install flask
RUN pip install pymongo
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY app.py /home/myapp/
COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD python3 /home/myapp/app.py
# CMD ["python3", "app.py"]

