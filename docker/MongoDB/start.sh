#!/bin/bash

# Запускаем MongoDB shell
mongo --host localhost --port 27017 -u $MONGO_USER -p $MONGO_PASSWORD --authenticationDatabase admin <<EOF
use $MONGO_DATABASE
db.createUser({
  user: "$MONGO_USER",
  pwd: "$MONGO_PASSWORD",
  roles: ["readWrite"]
})
use $MONGO_DATABASE
db.createCollection("user")
EOF
