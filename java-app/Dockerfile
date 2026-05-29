FROM maven:3.9-eclipse-temurin-21 AS builder

WORKDIR /app
COPY pom.xml .
COPY src/ src/

RUN mvn package

FROM eclipse-temurin:21-jre-alpine

WORKDIR /app
COPY --from=builder /app/target/hello-app-0.1.0.jar app.jar

ENV NAME=Intern

CMD ["java", "-jar", "app.jar"]
