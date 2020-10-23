# build
docker build -t fau-demo-image .

# recreate
docker rm  fau-demo-container --force
docker run --name fau-demo-container -p 5000:5000 fau-demo-image