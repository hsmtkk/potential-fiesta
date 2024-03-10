FROM python:3.11
WORKDIR /app
COPY front/requirements.txt /app/
RUN pip install -r requirements.txt
COPY front/ /app/
CMD streamlit run main.py --server.address 0.0.0.0 --server.port $PORT
