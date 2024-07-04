#!/bin/bash
# This script sends a request to a URL passed as the first argument, and displays the size of the body of the response
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2
