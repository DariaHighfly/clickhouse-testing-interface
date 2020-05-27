#!/usr/bin/env bash

cd test_data
for folder in *; do
    cd "$folder"
    python3 make_json.py
    cd ..
done
echo "ALL JSON FILES GENERATED SUCCESSFULLY!"

cd ..

cd clickhouse-testing-interface

npm run generate

echo "FINISHED! STATIC APP GENERATED SUCCESSFULLY!"

cd dist

open ./index.html

cd .. ..


