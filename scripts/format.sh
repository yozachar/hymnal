#!/bin/bash

# NOTE: song numbers that do not have writer's name abbrev:
# 116

START=1455
END=1510
for ((idx = START; idx <= END; idx++)); do
    file_path="hymnal/ag/${idx}.json"
    jq -c . <$file_path | tr -d '\n$' | sponge $file_path
    # trash $file_path
done
