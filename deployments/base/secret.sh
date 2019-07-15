#!/bin/bash -eux
DIR="$(dirname "$0")/secret"
mkdir -p "$DIR"
echo -n "$MACKEREL_APIKEY" > "$DIR/MACKEREL_APIKEY"
