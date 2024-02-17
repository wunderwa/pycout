# pycout
## (python console utils)

### bash history cleaner
Helper for HSTR - console utility
Removes duplicates. Adds preset commands to history (`included` key).
Removes frequent short commands (`excluded` key).
#### Init 
Copy `bash_history_cleaner-example.json` to `~/.bash_history_cleaner.json`
and edit. Json of file will be merged with `./bash_history_cleaner.json` presets.

Add bash file with exec rights `~/bin/hc`
```shell
#!/bin/bash
/user/work/wunderwa/pycout/bash_history_cleaner.py # path to cloned repo
```


Key `tags`["tag1","tag2"]  . Adds as `#tag1 #tag2 ...` to the end of preset command.
`cmd #tag1 #tag2`. It helps to search command like `#tag1 or #tag2`

```json
{
  "included": [
    {
      "cmd": "cd ~/work/company/project/",
      "tags": ["path", "work"]
    },
    {
      "cmd": "yarn fmt-changed",
      "tags": ["fmt"]
    }
  ],
  "excluded": [
    "git",
    "git status",
    "git branch",
    "git rebase --continue",
    "yarn",
    "yarn start"
  ]
}
```
