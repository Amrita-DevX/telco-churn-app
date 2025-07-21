# Use official Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy everything from your repo into the container
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Create .streamlit folder with config
RUN mkdir -p /app/.streamlit

# Add Streamlit config to prevent permission issues
RUN echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = 8501\n\
\n\
[browser]\n\
gatherUsageStats = false\n\
" > /app/.streamlit/config.toml

# Expose port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py"]