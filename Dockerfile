FROM python:3.13-alpine

WORKDIR /app

# Install build dependencies for Alpine
RUN apk add --no-cache gcc musl-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Remove build dependencies to reduce image size
RUN apk del gcc musl-dev

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]