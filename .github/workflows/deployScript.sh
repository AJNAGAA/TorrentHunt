# Due to a bug in appleboy/ssh-action@master, some commands shows error and fails to execute.
# So, running a bash file instead of commands

echo $1 > /opt/TorrentHunt/TorrentHunt/src/config.json  && pkill -f torrenthunt.py ; source /opt/TorrentHunt/venv/bin/activate && screen -dm python3 /opt/TorrentHunt/TorrentHunt/torrenthunt.py