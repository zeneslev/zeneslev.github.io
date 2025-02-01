#!/bin/bash
rm _posts/*
rm about.markdown
python3 update_blog.py
bundle exec jekyll build
git add .
echo "Enter Commit Message: "
read commitmsg
git commit -m "$commitmsg"
git push origin HEAD