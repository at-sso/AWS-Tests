#!/bin/bash

docker build -t locked-in-library ./zperk.t9/
docker run -p 5000:5000 locked-in-library
