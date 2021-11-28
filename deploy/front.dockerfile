FROM node:16-buster-slim

ENV YARN_CACHE_FOLDER=/cache/yarn

WORKDIR /app

# install dependencies
COPY front/package.json ./
RUN npm install


# copy app source
COPY front/ ./

CMD ["npm", "run", "serve"]
