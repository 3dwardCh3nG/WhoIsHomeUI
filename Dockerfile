# Here is the build image
FROM python:3-slim-buster as builder
RUN apt-get update \
    && apt-get install procps gcc -y \
    && apt-get clean
COPY requirements.txt /app/requirements.txt
WORKDIR app
RUN pip install --user -r requirements.txt
COPY WhoIsHomeUIDjango /app
COPY scripts /app/scripts

# Here is the production image
FROM python:3-slim-buster as app
ENV PYTHONUNBUFFERED=1
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app
RUN apt update \
    && apt install -y net-tools arp-scan \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*
WORKDIR app
ENV PATH=/root/.local/bin:$PATH

COPY --chown=1001 --from=builder /app/scripts /app/scripts
RUN chmod 0740 /app/scripts/*

EXPOSE 8008

CMD /app/scripts/entrypoint.sh