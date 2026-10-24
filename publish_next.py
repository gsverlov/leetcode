#!/usr/bin/env python3
"""Publish the next unpublished LeetCode solution from queue.json into solutions/ of a main-branch checkout.
Usage: python3 publish_next.py <queue.json> <repo_dir>
Prints the title published, or NONE_LEFT. Does not commit."""
import json, os, sys
queue, repo = sys.argv[1], sys.argv[2]
items = sorted(json.load(open(queue)), key=lambda x: x["ts"])
outdir = os.path.join(repo, "solutions")
os.makedirs(outdir, exist_ok=True)
for it in items:
    path = os.path.join(outdir, it["slug"] + ".py")
    if os.path.exists(path):
        continue
    header = f'# {it["title"]}\n# https://leetcode.com/problems/{it["slug"]}/\n\n'
    with open(path, "w", newline="\n") as f:
        f.write(header + it["code"].rstrip() + "\n")
    print(it["title"])
    break
else:
    print("NONE_LEFT")
