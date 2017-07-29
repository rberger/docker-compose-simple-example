# Docker Compose Example with Consul

Started from https://www.sumologic.com/blog/devops/how-to-build-applications-docker-compose/

Only differences
* Used the more modern Docker for Mac
  * It uses the builtin Hyperkit of Docker for MacOS
  *  __DID NOT USE docker-machine__
  * No longer a need to have the `link:` as docker-compose will automatically
    create a default network and make the service names usable without the
    `link:`
* Was able to access the docker containers that expose ports using `localhost` on my Mac
  * Was able to browse to http://localhost for accessing the NGINX
  * Was able to browse to http://localhost:8500 to access the Consul UI
    * Could see the key/value set by the python application
    * Could update the value in the Consul UI and see the result in the NGINX/Python app on refreshing http://localhost
* Did not use `localhost` to reference between containers, used the `service name`
* Added a Consul just like in irmin
  * No need for `container_name` in the docker_compose
