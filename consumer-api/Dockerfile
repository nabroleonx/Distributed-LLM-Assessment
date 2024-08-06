FROM node:18-alpine

RUN npm install -g pnpm

WORKDIR /app

COPY consumer-api/package.json ./
RUN pnpm install

COPY consumer-api .

EXPOSE 3000

CMD ["pnpm", "start"]
