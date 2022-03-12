#!/usr/bin/env bash
if [ $# -eq 1 ]; then
    git add . && git commit -m "$1" && git push

elif [ $# -eq 0 ]; then
   git add . && git commit -m "Submit" && git push
fi
