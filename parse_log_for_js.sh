#!/bin/bash

# Simply parses a web server access log (created for apache) for unique Javascript filenames
# Sorts and lists them
# The regex was good enough for my needs

cat "$1" | grep -oP '[^/]*\.js(?![a-zA-Z0-9])' | sort -u
