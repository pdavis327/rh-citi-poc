#!/bin/bash
## update this file to run a series of commands

docker compose run --rm pipeline_template \
training \
--source_training_data=assets/iris.csv
