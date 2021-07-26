<h1>Perfsys Tesk Task by Kostiantyn Kertsman</h1>



<h3>Languages and tools used in project:</h3>
<p align="left"> <a href="https://aws.amazon.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a>
<a href="https://serverless.com" target="_blank"> <img src="https://github.com/serverless/artwork/blob/1701ae94377700fde0496890d26a6851720a4f9a/icon-serverless.png" alt="serverless" width="40" height="40"/> </a> 
<a href="https://serverless.com" target="_blank"> <img src="https://github.com/serverless/artwork/blob/1701ae94377700fde0496890d26a6851720a4f9a/icon-serverles-framework.png" alt="serverless" width="40" height="40"/> </a> 
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

<h2> REQUIRES SERVERLESS FRAMEWORK </h2>

# Install plugin for requirements:
You need to install plugin for requirements with sls manager:
```bash
$ sls plugin install -n serverless-python-requirements

```

# Deploy

```bash
$ sls deploy

```

# Test it
For working with project use <a href="https://www.postman.com">Postman</a> or CURL 

Links for working with project you can find in terminal after deployment:

<kbd><img src="https://github.com/kokakerze/serverlessblob/blob/c84686bcaae864a036047aa4110c971cfbb97c40/blobs/1.png"/></kbd>

Mac:
```bash
$ brew install curl

```
Linux:

```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install curl
```

<h3>Also you can test it by my own links:</h3>

  POST - "https://8as291eds6.execute-api.eu-central-1.amazonaws.com/blobs"

  GET - "https://8as291eds6.execute-api.eu-central-1.amazonaws.com/blobs/{id}"
