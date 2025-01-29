#!/bin/bash
rm _posts/*
python3 update_blog.py
bundle exec jekyll build
git add .
git commit -m "new version"
git push origin HEAD
mattkrolick@gmail.com
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