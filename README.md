# MWDB Feeds

[![build](https://travis-ci.org/c3rb3ru5d3d53c/mwdb-feeds.svg?branch=master)](https://travis-ci.org/c3rb3ru5d3d53c/mwdb-feeds)
[![license](https://img.shields.io/github/license/c3rb3ru5d3d53c/mwdb-feeds)](https://github.com/c3rb3ru5d3d53c/mwdb-feeds/blob/master/LICENSE)
[![pypi-version](https://pypip.in/v/mwdb-feeds/badge.png)](https://pypi.org/project/mwdb-feeds/)
[![pypi-downloads](https://pypip.in/d/mwdb-feeds/badge.png)](https://pypi.org/project/mwdb-feeds/)
[![pypi-wheel](https://pypip.in/wheel/mwdb-feeds/badge.svg)](https://pypi.org/project/mwdb-feeds/)
[![issues](https://img.shields.io/github/issues/c3rb3ru5d3d53c/mwdb-feeds)](https://github.com/c3rb3ru5d3d53c/mwdb-feeds/issues)
[![stars](https://img.shields.io/github/stars/c3rb3ru5d3d53c/mwdb-feeds)](https://github.com/c3rb3ru5d3d53c/mwdb-feeds/stargazers)

A Modular MWDB Utility to Collect Fresh Malware Samples

This project is FREE as in FREE :beer:, use it commercially, privately or however you see fit.

If you like this project and wish to donate :moneybag: to support the fight against malware...

Buy me a :tea:, as I don't drink :beer:, by sending me some ₿ to `16oXesi7uv3jdPZxxwarHSD2f3cNMpaih9`

**Installation from Source:**
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

**Installation from PyPi:**
```bash
sudo apt install -y python3-virtualenv python-is-python3
virtualenv venv/
source venv/bin/activate
pip install mwdb-feeds
git clone https://github.com/c3rb3ru5d3d53c/mwdb-feeds-modules.git modules/
find modules/ -name "requirements.txt" | while read i; do pip install -r $i; done
nano mwdb-feeds.ini                                       # Edit your Configuration File
mwdb-feeds --config mwdb-feeds.ini --list-modules         # List Modules
mwdb-feeds --config mwdb-feeds.ini --module malwarebazaar # Run Single Module
mwdb-feeds --config mwdb-feeds.ini                        # Run All Module
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

To regularly update your instance try using `cron`.

**Contributing:**

If you wish to contribute your own modules, please refer to [CONTRIBUTING.md](https://github.com/c3rb3ru5d3d53c/mwdb-feeds/blob/master/CONTRIBUTING.md)
