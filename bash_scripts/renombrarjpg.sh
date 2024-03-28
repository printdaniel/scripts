#!/bin/bash

contador=1

for archivo in *.jpg; do
    anahi="anahi$contador.jpg"
    mv "$archivo" "$anahi"
    ((contador++))
done
