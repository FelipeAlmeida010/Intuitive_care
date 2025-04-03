FROM postgres:latest

COPY scripts /scripts
RUN chmod +x /scripts/init_db.sh

ENTRYPOINT ["/bin/bash", "/scripts/init_db.sh"]
