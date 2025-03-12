# Trellis challenge!

This repository implements an application that converts numbers into English words.
This is an answer to the Trellis challenge.

## Instructions

### Dependencies

- Docker

### Executing the application

To execute the application, go to the project root directory and run:
```
make run
```

#### Accessing the application

With the application running, open a web browser and access:
```
http://localhost/test
```

Then try it!

![image](https://github.com/user-attachments/assets/fc795ef2-eee4-4a4d-80dc-dd2919d5bb9c)

#### Accessing the documentation

With the application running, open a web browser and access:
```
http://localhost:8000/docs
```
![image](https://github.com/user-attachments/assets/043241b3-8679-4238-9b21-2d72e7321a2d)

### Executing unit tests

Go to the project root directory and run:
```
make test
```

### Validating the API

#### Making a GET request

With the application running, run:
```
curl http://localhost:8000/num_to_english\?number\=123
```

The response should be like:
```
{"status": "ok", "num_in_english": "one hundred twenty three"}
```

In the backend log stream, you should see something like:
```
backend-1   | [INFO] [2025-03-10 22:14:43] [views.py:37] - <rest_framework.request.Request: GET '/num_to_english?number=123'>
```

#### Making a POST request

With the application running, run:
```
curl http://localhost:8000/num_to_english -X POST -d '{"number": "123"}'
```

Response should be like:
```
{"status": "ok", "num_in_english": "one hundred twenty three"}
```

In the backend log stream, you should see something like:
```
backend-1   | [INFO] [2025-03-10 22:16:19] [views.py:60] - <rest_framework.request.Request: POST '/num_to_english'>
backend-1   | [INFO] [2025-03-10 22:16:19] [views.py:61] - b'{"number": "123"}'
```

#### Discussion points

##### Errors

The log of errors is persistent. Even if the  container terminates, historical records will be found at `logs/errors.log`.

##### Throttling

Regarded that this should be a public endpoint, requests are limited to a maximum of 5 requests per second to prevent overloading the application server. Any further requests beyond this limit will result in status code **429** (Too Many Requests Error).

##### Formatting

Libraries `black` and `flake8` are utilized to format the code in the backend. Library `prettier` is utilized to format the code on the front end.

##### Architecture

This application comprises a Django backend and a SPA frontend written in VueJS with Tailwind. Both parts run within isolated container images and are separately served for HTTP via NGINX.

![image](https://github.com/user-attachments/assets/4119ca1d-a0ae-44ce-9f54-704f254942d9)

