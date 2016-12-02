#!/usr/bin/env bash

SCRIPT_BASE_NAME=`basename "$0"`

cd `dirname $0`

rm -rf test/*
swagger-codegen generate -l python -i swagger.json -c config-swagger

git apply patchs/*.patch
