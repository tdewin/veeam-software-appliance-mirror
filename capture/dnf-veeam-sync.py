#!/usr/bin/env python3
import subprocess
from urllib.parse import urlparse
import dnf


base = dnf.Base()

base.conf.read(priority=dnf.conf.PRIO_MAINCONFIG)
base.conf.substitutions.update_from_etc(installroot=base.conf.installroot, varsdir=base.conf.varsdir)
base.read_all_repos()

alllogs = ["Synced:"]
veeamrepos = {k: v for k, v in base.repos.items() if k.startswith("veeam-")}
for repoid in veeamrepos:
  repo = base.repos[repoid]
  url = repo.baseurl[0]
  parsed = urlparse(url)
  path_only = parsed.path.lstrip("/")
  log = f'{repoid} {url} > /mirror/{path_only}'
  print(f"Running {log}")
  alllogs.append(log)
  torun = ["dnf","reposync","--download-meta","-p",f"/mirror/{path_only}","--norepopath","--repo",repoid]
  subprocess.run(torun)

print("\n".join(alllogs))
