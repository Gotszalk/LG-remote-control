# LG Remote Control app
This is remote control flask app (Python+HTML) for LG TV on WebOS. 

## Requirements
Requirements are as follows:
  * aiowebostv
  * flask
  * gunicorn
  * wakeonlan
  * uvicorn
  * fastapi

Info: Development environment does not require gunicorn!

## Initial configuration
1. Get IP address and MAC address of your LG TV e.g. your home router may clearly show the info or directly check network settings on your TV.
2. Edit ./rcontrol/tools/get_key.py and add correct IP address.
3. Run the script to get client key <code>python get_key.py</code>
4. Add client key, TV IP address and TV MAC address to ./rcontrol/lib/tv_data.json

App is ready to control your TV.

## FastAPI Microservice
Due to issues with gunicorn vs multiprocessing, the signal sender functionality required to be rewritten as microservice. As simple as possible solution was FastAPI. 

I considered flask to flask communication but it would require separate production instance of flask which would be additional complication.

## Execution
App can be started by executing:
1. <code>./rcontrol/run_ms</code> - execution of FastAPI microservice to send signals to TV
2. <code>./webapp/run</code> - execution of flask app with remote control GUI

## Dockerization
There was a plan to dockerize both services but managing a client key became a problem since a container is like another machine and requires separate key. Dockerfiles are available and working:

<code>
 cd rcontrol
 podman build --tag rcontrol .
</code>

<code>
 cd webapp
 podman build --tag rc_webapp .
</code>

Running containers:

<code>
 cd rcontrol
 podman run -it -p 8000:8000 rcontrol
</code>

<code>
 cd webapp
 podman run -it -p 8001:8001 rc_webapp
</code>

Again, rcontrol requires client key for specific environment which has to be confirmed on the TV. In efect, running as a docker is problematic. However, code has been cleaned and folder structure reflects logic of 2 separate services. Additionaly gunicorn does not need gevent since async calls are only in FastAPI microservice.
