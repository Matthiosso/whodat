FROM postgres:13.4-alpine

COPY db/init-sql/* /docker-entrypoint-initdb.d/
