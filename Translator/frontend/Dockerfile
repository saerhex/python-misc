FROM node:lts-buster-slim

WORKDIR /project
COPY package.json /project
COPY yarn.lock /project

RUN npm install yarn
RUN yarn install

CMD ["yarn", "start"]