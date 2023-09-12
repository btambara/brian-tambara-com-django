FROM node:20-alpine AS node

WORKDIR /site_media

COPY www .

RUN npm install

RUN npm run build

FROM python:3.11

WORKDIR /app

COPY --from=node site_media/dist dist

COPY brian_tambara_com .

COPY setup/requirements.txt requirements.txt

RUN pip install -r requirements.txt
