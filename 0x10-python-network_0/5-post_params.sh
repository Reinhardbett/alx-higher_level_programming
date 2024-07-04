#!/bin/bash
# send a POST request to URL and display response body
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I wll always be here for PLiD"
