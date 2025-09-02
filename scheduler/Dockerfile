FROM python
WORKDIR /home/myapp/ 
COPY ./database.py .
COPY ./producer.py .
COPY ./scheduler.py .
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD python3 scheduler.py
# seee chotipat2025