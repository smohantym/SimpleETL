FROM apache/spark-py

USER root

# Set working directory
WORKDIR /app

# Copy application code
COPY app/ /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["spark-submit", "--master", "local[*]", "etl.py"]
