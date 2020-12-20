#!/bin/sh
# wait-for-sut.sh

set -e
  
host="$1"
shift
cmd="$@"
  
until http --quiet GET "$host"; do
  >&2 echo "SUT is unavailable - sleeping for 3 seconds..."
  sleep 3
done
  
>&2 echo "SUT is up - starting tests..."
exec $cmd