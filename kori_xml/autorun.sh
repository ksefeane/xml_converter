#! /usr/bin/bash

mkdir CSV
for file in *.xml
do
    echo "Target: $file"
    python3 convert.py "$file"
    echo "$file converted"
    mv *.csv CSV
done