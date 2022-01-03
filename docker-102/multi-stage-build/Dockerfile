# 建立一個名為 builder 的暫存 Image，用來打包程式碼
FROM maven:3.8.4-openjdk-8-slim as builder
WORKDIR /workspace
# 複製程式碼至 /workspace
COPY ./spring-boot /workspace
# 打包程式碼
RUN  unset MAVEN_CONFIG && ./mvnw package

# Runtime Container 選用盡可能小的 Image，也不需要任何打包工具，因此選用 openjdk:8-jdk-alpine
FROM openjdk:8-jdk-alpine
WORKDIR /app
# 從上方暫存的 builder Image 複製 jar 檔至 /app 目錄中
COPY --from=builder /workspace/target/spring-boot-complete-0.0.1-SNAPSHOT.jar /app/app.jar
EXPOSE 8080
# 最後生成的 Image 在執行時直接啟動 app.jar
CMD ["java", "-jar", "app.jar"]
