FROM maven:3.9.6-eclipse-temurin-17 AS builder
WORKDIR /build
COPY app/pom.xml .
COPY app/src ./src
RUN mvn clean package -DskipTests

FROM eclipse-temurin:17-jre-jammy
WORKDIR /app
RUN useradd -u 1001 appuser && chown -R appuser /app
USER appuser
COPY --from=builder /build/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
