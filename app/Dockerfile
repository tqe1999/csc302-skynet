FROM node:lts

RUN addgroup --system reactjs
RUN adduser --system --ingroup reactjs reactjs
WORKDIR /reactjs
COPY . .
RUN npm ci
USER reactjs
ENTRYPOINT ["npm", "start"]
