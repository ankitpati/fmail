#!/usr/bin/env bash

exec curl -d @'simple_email.json' -H 'Content-Type: application/json' \
          'http://localhost:8000'
