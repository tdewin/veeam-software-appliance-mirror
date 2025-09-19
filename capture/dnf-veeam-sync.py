#!/usr/bin/env python3
import subprocess
from urllib.parse import urlparse

result = subprocess.run(['dnf', 'repolist', 'veeam-*','-v'], capture_output=True, text=True)

id = ""
for ln in result.stdout.split("\n"):
  words = ln.split(":")
  if len(words) > 1:
    firstword = words[0].strip().lower()
    remainder = ":".join(words[1:]).strip()
    if (firstword == "repo-id"):
      id = remainder
    elif (firstword == "repo-baseurl"):
      parsed = urlparse(remainder)
      path_only = parsed.path.lstrip("/")
      torun = ["dnf","reposync","--download-meta","-p",f"/mirror/{path_only}","--norepopath","--repo",id]
      subprocess.run(torun)
