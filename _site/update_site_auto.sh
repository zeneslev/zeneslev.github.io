#!/bin/bash
rm _posts/*
rm about.markdown
python3 update_blog.py
bundle exec jekyll build
git add .
git commit -m "auto commit go!"
git push origin HEAD