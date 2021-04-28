# Contributing a MWDB Feed Module

**Step 1: Download the Main Repository**

```bash
git clone --recursive https://github.com/c3rb3ru5d3d53c/mwdb-feeds.git
cd mwdb-feeds/modules/
```

**Step 2: Create your Module Directory**
```bash
mkdir example/
cd example/
touch README.md requirements.txt example.py
```

- `README.md` A description of your module
- `requirements.txt` Dependancies of your module (should include versions)
- `example.py` Your module code

**Step 3: Write your Module**
```python
#!/usr/bin/env python

import logging

log = logging.getLogger(__name__)

__author__  = 'c3rb3ru5'
__version__ = '1.0.0'


class MWDBFeedsModule():

    """
    An Example MWDB Feed Module
    """

    def __init__(self, config, mwdb):
        self.name = 'example'               # Name of your Module
        self.tag  = f'feed:{self.name}'     # Feed Tag
        self.enabled = self.startup(config) # Check Configuration File
        self.mwdb = mwdb                    # Set the mwdblib object

    def startup(self, config):
        options = ['enabled', 'file']
        for option in options:
            if config.has_option(self.name, option) is False:
                log.warn(f'{self.name} section is missing the {option} option')
                return False
        self.config = config
        return True

    def main(self) -> dict:
        result = {
            'module': self.name,
            'success': True
        }
        try:
            f = open(self.config.get(self.name, 'file'), 'rb')
            content = f.read()
            name = hashlib.sha256(data).hexdigest()
            upload = self.mwdb.upload_file(name=name, content=content)
            upload.add_tag(self.tag)
            f.close()
        except Exception as error:
            log.error(error)
            result['success'] = False
        return result
```

**Step 4: Add your Configuration**

Apppend this configuration to your existing `mwdb-feeds.ini` file.
```ini
[example]
enabled = True
file = example.bin
```

**Step 5: Test your Module**
```bash
$ mwdb-feeds --config mwdb-feeds.ini --module example
```

**Step 6: Contribute**

Send a pull request so other can use your module as well.
