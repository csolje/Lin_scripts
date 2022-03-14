#!/usr/bin/env bash
filename=$1
while IFS= read -r line; do
# Reading files lines
echo "$line"
ping -c 2 $line
done <$filename