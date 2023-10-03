FROM mysql:8.1.0

# mysql reads this and create db accordingly
#ENV MYSQL_DATABASE marvel

# init scripts copied at build
COPY ./scripts/ /docker-entrypoint-initdb.d/

