# Use the official Python 3.11 base image from Docker Hub
FROM python:3.11

# Set the working directory inside the container
WORKDIR /MULTI-TOOL
# Copy all your Python files and requirements.txt into the container
COPY . /MULTI-TOOL/

# Install necessary network tools
RUN apt-get update && apt-get install -y \
    iproute2 \
    net-tools \
    wireless-tools \
    pciutils \
    network-manager

# Install the necessary libraries
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python program (multi_tool.py)
CMD ["python", "multi_tool.py"]

# Build command
# docker build -t multi-tool-app .

# Run program
# docker run -it multi-tool-app .