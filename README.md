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

## Initial configuration
1. Get IP address and MAC address of your LG TV e.g. your home router may clearly show the info or indirectly check network settings of your TV.
2. Edit ./tools/get_key.py and add correct IP address.
3. Run the script to get client key <code>python check_key.py</code>
4. Add client key, TV IP address and TV MAC address to ./lib/tv_data.json

App is ready to control your TV.

## Development environment
App can be started by executing:
<code>python app.py</code>

Info: Development environment does not require gunicorn!

## Production environment
For production purposes it is required to install WSGI e.g. gunincorn.
<code>pip install gunicorn</code>

App can be started by:
<code>./run </code>

## FastAPI Microservice
Due to issues with gunicorn vs multiprocessing, the signal sender functionality required to be rewritten as microservice. As simple as possible solution was FastAPI. 

I considered flask to flask communication but it would require separate production instance of flask which would be additional complication.

## Execution
Switching to signal sender in microservice requires sequential execution as follows:
1. Run sender in microservice 
<code>
cd ./microservice/
./run_ms
</code>
2. Run gunicorn <code>./run</code>

## Dockerization
There was a plan to docekrize both services but managing a TV key became a problem since a container is like separate machine. Dockerfiles are available and working:
<code>podman build --tag rcontrol .</code>
<code>podman build --tag rc_webapp .</code>
Running:
<code>podman run -it -p 8000:8000 rcontrol</code>
<code>podman run -it -p 8001:8001 rc_webapp</code>
Again, rcontrol requires tv key for specific environment which has to be confirmed on the TV. In efect, running as a docker is problematic. However, code has been cleaned and folder structure reflects logic of 2 separate services. Additionaly gunicorn does not need gevent since async calls are only in FastAPI microservice.
