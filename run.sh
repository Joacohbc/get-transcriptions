#!/bin/bash
docker build -t youtube-transcriber .
docker run -v $(pwd):/app youtube-transcriber