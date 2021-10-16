
<h1 align="center"> M3U generator </h1>

[![M3U generator for YouTube](https://github.com/chungstudio/ChungTV/actions/workflows/m3u_Generator.yml/badge.svg)](https://github.com/chungstudio/YouTube_to_m3u/actions/workflows/m3u_Generator.yml)

`https://raw.githubusercontent.com/chungstudio/ChungTV/main/playlist.m3u`

Updated m3u links of YouTube live channels, **auto-updated every hour**.


### Add more channels
Edit `youtube_channel_info.txt` to add your favourite YouTube livestreams
### Usage
Paste this URL: `https://raw.githubusercontent.com/chungstudio/ChungTV/main/playlist.m3u` to any player which supports M3U playlists

### Run the tool on your local machine
``` bash
git clone https://github.com/chungstudio/ChungTV.git
cd YouTube_to_m3u
chmod +x autorun.sh
./autorun.sh
```

Do not forget to add a cron job set for every 4 hours(or 5) if you plan to run the script locally.
