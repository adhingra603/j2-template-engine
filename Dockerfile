FROM python:3-alpine

# Common pkgs
RUN apk update
RUN apk add bash

# Tool location
ENV RENDER_HOME=/usr/local/bin

# Add tool to container
WORKDIR ${RENDER_HOME}
ADD requirements.txt .
ADD render.py .
RUN pip install -r requirements.txt

# Create user
RUN adduser -D overwatch
USER overwatch
WORKDIR /home/overwatch

ENTRYPOINT ["render.py"]
CMD ["-h"]
