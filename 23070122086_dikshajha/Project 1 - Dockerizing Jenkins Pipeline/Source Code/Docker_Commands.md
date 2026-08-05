# Docker Commands Used

## Build Docker Image

```bash
docker build -t helloworldflask_tw1-flask-app .
```

## List Docker Images

```bash
docker images
```

## Run Docker Container

```bash
docker run -d -p 5000:5000 helloworldflask_tw1-flask-app
```

## List Running Containers

```bash
docker ps
```

## Stop Container

```bash
docker stop <container_id>
```

## Remove Container

```bash
docker rm <container_id>
```

## Remove Docker Image

```bash
docker rmi helloworldflask_tw1-flask-app
```