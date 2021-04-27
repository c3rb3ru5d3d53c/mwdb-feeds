# MWDB Feeds

[![build](https://travis-ci.org/c3rb3ru5d3d53c/mwdb-feeds.svg?branch=master)](https://travis-ci.org/c3rb3ru5d3d53c/mwdb-feeds)
[![license](https://img.shields.io/github/license/c3rb3ru5d3d53c/mwdb-feeds)](https://github.com/c3rb3ru5d3d53c/mwdb-feeds/blob/master/LICENSE)
[![issues](https://img.shields.io/github/issues/c3rb3ru5d3d53c/mwdb-feeds)](https://github.com/c3rb3ru5d3d53c/mwdb-feeds/issues)
[![stars](https://img.shields.io/github/stars/c3rb3ru5d3d53c/mwdb-feeds)](https://github.com/c3rb3ru5d3d53c/mwdb-feeds/stargazers)

A Modular MWDB Utility to Collect Fresh Malware Samples

This project is FREE as in FREE :beer:, use it commercially, privately or however you see fit.

If you like this project and wish to donate :moneybag: to support the fight against malware...

Buy me a :tea:, as I don't drink :beer:, by sending me some ₿ to `16oXesi7uv3jdPZxxwarHSD2f3cNMpaih9`

**Installation:**
```bash
sudo apt install -y python3-virtualenv python-is-python3
git clone --recursive https://github.com/c3rb3ru5d3d53c/mwdb-feeds.git
cd mwdb-feeds/
virtualenv venv/
source venv/bin/activate
./setup.py install
nano mwdb-feeds.ini                                            # Edit your Configuration File
mwdb-feeds --config-file mwdb-feeds.ini --list-modules         # List Modules
mwdb-feeds --config-file mwdb-feeds.ini --module malwarebazaar # Run Single Module
mwdb-feeds --config-file mwdb-feeds.ini                        # Run All Modules
```

**Configuration:**
```ini
[mwdb-feeds]
threads = 1
modules = modules/
debug = True
log = False
url = https://mwdb.local/api/
username = <your_username_here>
api_key = <your_api_key_here>
verify_ssl = True
```

**Contributing:**

If you wish to contribute your own modules to automatically unpack malware, please refer to [CONTRIBUTING.md](https://github.com/c3rb3ru5d3d53c/mwdb-feeds/blob/master/CONTRIBUTING.md)
