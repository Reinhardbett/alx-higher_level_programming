#!/bin/bash
# send request to URL and display only status code
curl -o /dev/null -s -w "%{http_code}" "$1"
