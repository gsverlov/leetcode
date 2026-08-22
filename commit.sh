#!/bin/bash
cd /c/Users/gsv/source/repos/Leetcode || exit 1
git add -A
git diff --cached --quiet && exit 0
git commit -m "LeetCode practice $(date +%F)"
git push origin main
