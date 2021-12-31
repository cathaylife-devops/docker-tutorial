# Build Image

Goals:

1. build & run
2. push code to github(gitlab/bitcucket)
3. push image to dockerhub

```bash
# step 1: build & run
docker build -t demo-image:v0.1.0 .
docker run --rm demo-image:v0.1.0

# step 2: push code to github(gitlab/bitcucket)
# step 3: push image to dockerhub
```
