#!/bin/bash

set -e

cd web/
npm install
npm run build
cp -rf build/* ../modules/app/dist/
cd ..
docker-compose up --build