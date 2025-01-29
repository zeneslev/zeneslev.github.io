#!/bin/bash
rm _posts/*
python3 update_blog.py
bundle exec jekyll build
git add .
git commit -m "new version"
git push origin HEAD