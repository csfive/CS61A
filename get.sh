#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <assignment> (e.g. ./get.sh lab00)"
    exit 1
fi

NAME=$1
TYPE=${NAME//[0-9]/}
[ "$TYPE" = "$NAME" ] && TYPE="proj"
URL="https://cs61a.vercel.app/${TYPE}/${NAME}/${NAME}.zip"

echo "🎯 Target: $URL" && \
wget -q "$URL" && \
unzip -q "${NAME}.zip" && \
echo "✨ $NAME is ready!"
