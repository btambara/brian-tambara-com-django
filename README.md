# brian-tambara-com

## Development Environment Setup

### Setup a Python Virtual Environment

``` bash
python -m venv venv
```

### [pip-tools](https://pypi.org/project/pip-tools/) Installation

``` bash
pip install pip-tools
pip-sync setup/requirements.txt
```

### Setup [Vite](https://vitejs.dev/) Environment

``` bash
cd www
npm install
```

Learn more [here](./www/README.md)

## Running locally

``` bash
docker-compose up -d --build
```
