# FAU CEN5035 DEMO: Python REST API in Docker

## Check Python Version & PIP

We need python version 3 and `pip` to install dependencies.

```
python --version
python -m pip --version
```

## Install Flask

What is Flask - https://palletsprojects.com/p/flask/

```
pip install --no-cache-dir -r requirements.txt
or 
python -m pip install flask
```

## Run Application

```
python server.py
```

![FAU Pic](/static/images/fau-demo.png)

## Browse / Test it

* Home: http://localhost:5000/
* List Messages: http://localhost:5000/messages/list
* Add Message (success): http://localhost:5000/messages/add?message=Any%20message%20I%20want%20can%20go%20here
* Add Message (fail): http://localhost:5000/messages/add

## Docker

Get Docker Desktop and explore the python docker packages.

* https://hub.docker.com/editions/community/docker-ce-desktop-windows
* https://hub.docker.com/_/python

## Build / Run Docker Contailer Locally

You can simply run the build & run scripts, or execute commands side-by-side.

```bash
# windows
./scripts/run.ps1

# linux
./scripts/run.sh
```

Alternatively you can execute the docker commands independently. Note that we create `fau-demo-image` that is used to create the container `fau-demo-container`.

```bash
# build
docker build -t fau-demo-image .

# remove container to prevent creation error
docker rm  fau-demo-container --force

# create new container
docker run --name fau-demo-container -p 5000:5000 fau-demo-image
```

Helpful links:

* Docker Build: https://docs.docker.com/engine/reference/commandline/build/
* Docker Run: https://docs.docker.com/engine/reference/run/
* Docker Tutorial: https://docs.docker.com/get-started/part2/


## Cloud Provider Links

* AWS - https://aws.amazon.com/education/awseducate/
* Azure - https://docs.microsoft.com/en-us/learn/azure/


## AWS & Azure Resources for Students

* https://azure.microsoft.com/en-us/free/students/
* https://aws.amazon.com/about-aws/whats-new/2015/05/aws-educate-students-and-educators-can-access-aws-technology-cloud-courses-training-and-collaboration-tools/
