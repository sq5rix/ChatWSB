# Use the official Ubuntu base image
FROM python:3.11-bookworm

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Run the specified command within the container
CMD ["python", " -m spacy download pl_core_news_lg"]

