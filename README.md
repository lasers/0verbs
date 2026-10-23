# 0verbs
Download (local .txt database) and search for OpenBSD package. No need to use the package searching (or set `PKG_PATH`) as it takes too long to list and find your query and you are required to have internet up and running.

Download this fellow and run it without any arguments, so it can download small `.txt` database first:

```bash
python 0verbs.py

# to query the database
python 0verbs.py 'curl'

# or use the slow option
pkg_info -aQ 'curl'
```