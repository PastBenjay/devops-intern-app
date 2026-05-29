FROM alpine:3.19 AS base

WORKDIR /app
COPY run.sh .
COPY tests/ tests/
RUN chmod +x run.sh tests/test_run.sh

FROM base AS test
RUN ./tests/test_run.sh

FROM base AS final
ENV NAME=Intern
CMD ["/bin/sh", "./run.sh"]
