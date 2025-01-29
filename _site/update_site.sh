#!/bin/bash
bundle exec jekyll build
git add .
git commit -m "new version"
git push origin HEAD