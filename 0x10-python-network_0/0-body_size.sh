#!/bin/bash
# Retrieve and display the content of a URL
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
