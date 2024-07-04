#!/bin/bash
# send GET request and header variable
curl -s -X GET "$1" -H"X-School-User-Id: 98"
