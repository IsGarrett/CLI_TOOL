
#!/bin/bash

current_time=$(date "+%H:%M")

if [ "$current_time" == "20:21" ]; then
  scp -P 2222 "/Users/garrettlambert/Code Projects/CLI Folder/automator.py" parallels@127.0.0.1:/home/parallels/CLI_TOOL
fi
