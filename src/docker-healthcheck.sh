#!/bin/bash
set -ex

echo 1 > test.log

cd tests
  python ./test.py |tee ./test.log
cd ..

