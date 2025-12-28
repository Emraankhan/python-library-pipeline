FROM python:3.9-slim

WORKDIR /app

# Copy all files from your current folder into the container
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Run the automator from the root now
CMD ["python", "automator.py"]