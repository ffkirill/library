#!/usr/bin/env bash
while true; do \
  make; \
  inotifywait -qre close_write src/; \
done
