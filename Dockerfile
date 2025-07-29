# base model Python 3.11.5, but we use python 3.11-slim
# Slimmed-down version of the latest 3.11 release.
# Based on debian, but stripped of unnecessary files like man pages, docs, dev tools.
# Much smaller in size (~30–50% smaller than the full version).
# Suitable for production, where smaller image size = faster deploys.
FROM python:3.11-slim

# set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .

# RUN pip install -r requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of application code
COPY . .

# Expose the application port (port number depend on what kind application we made)
EXPOSE 8000

# Command to start FAST API application

CMD ["uvicorn","app_ML_model:app", "--host", "0.0.0.0","--port","8000"]

