#!/bin/bash
for jsonFile in $(ls /data/files/*.json); do
    mongoimport --host localhost -u gastos -p gastos --db gastosdb --collection gastos --type json --file $jsonFile --jsonArray
done
