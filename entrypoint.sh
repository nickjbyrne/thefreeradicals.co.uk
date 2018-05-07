#!/bin/sh

cd /usr/src/app/output
python -m pelican.server $PORT $ADDR
