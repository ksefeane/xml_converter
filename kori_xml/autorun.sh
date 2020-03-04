#! /usr/bin/bash


for file in *.xml
do
    echo "Target: $file"
    python3 convert.py "$file"
    echo "File converted"
done
mv *.csv CSV
