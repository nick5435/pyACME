#!/bin/bash
CSTRING="Autocommit at $(date '+%Y-%m-%d %H:%M:%S')"
git add .
git commit -m "\"$CSTRING\""
git push origin
python -m build --no-isolation 
twine upload -r testpypi dist/*
twine upload dist/*