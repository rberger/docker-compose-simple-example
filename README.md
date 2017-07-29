# Sumo Compose Example

From https://www.sumologic.com/blog/devops/how-to-build-applications-docker-compose/

Only difference is I used the more modern Docker for Mac that DOES NOT USE
docker-machine. It uses the builtin Hyperkit of Docker for MacOS

So to access the docker services I was able to browse on my Mac browser to
http://localhost or for the earlier part without nginx I was able to browse to
http://localhost:5000 Actually to http://localhost:5010 as I changed the ports
to use host port 5010 since I have something running on 5000 on my Mac.

The initial config I had for accessing the python app without nginx was:

```
version: '2'
services:
  helloworld:
    image: helloworld:1.0
    ports:
    - "5010:5000"
    volumes:
    - ../helloworld:/code
```

Also there is no longer a need to have the `link:` as docker-compose will
automatically create a default network and make the service names usable without
the `link:`

