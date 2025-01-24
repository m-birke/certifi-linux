#!/bin/bash

rm -rf ./dist/*.whl
hatch build -t wheel
