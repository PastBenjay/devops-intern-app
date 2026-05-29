FROM alpine:3.19

WORKDIR /app

COPY run.sh .
COPY tests/ tests/

RUN chmod +x run.sh tests/test_run.sh

ENV NAME=Intern

CMD ["./run.sh"]
