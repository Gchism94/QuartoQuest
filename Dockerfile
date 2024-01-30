# Use a Python base image
FROM python:3.8-slim

# Install wget, Git, and other necessary tools
RUN apt-get update && apt-get install -y \
    wget \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Quarto
RUN wget -q -O quarto.deb https://github.com/quarto-dev/quarto-cli/releases/download/v1.1.189/quarto-1.1.189-linux-amd64.deb && \
    dpkg -i quarto.deb && \
    rm quarto.deb

# Create a non-root user
RUN useradd --create-home autograder
WORKDIR /home/autograder

# Copy only the requirements.txt initially to leverage Docker cache
COPY --chown=autograder:autograder requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Set the working directory to the 'quartoquest' subdirectory
WORKDIR /home/autograder/quartoquest

# Copy the 'quartoquest' directory
COPY --chown=autograder:autograder quartoquest/ ./

# Install the application (editable mode)
RUN pip install -e .

# Command to run on container start
CMD ["python", "autograder.py"]