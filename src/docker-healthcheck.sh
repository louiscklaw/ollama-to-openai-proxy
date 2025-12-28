#!/bin/bash
set -ex

echo 1 > test.log

cd tests
  python ./test.py |tee ./test.log
cd ..

curl https://healthcheck.iamon99.com/ping/9b230bf0-8fca-4bb3-b83d-ab443dd1d32c
