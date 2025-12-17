# YT Downloader scripts

This repository provides a small utility setup for downloading YouTube content using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp/), with explicit handling of authenticated sessions via exported cookies. It documents how to extract and convert browser cookies, prepare the Python environment, run the download script.

- [YT Downloader scripts](#yt-downloader-scripts)
  - [Manage Cookies](#manage-cookies)
    - [Exporting YouTube cookies - Overview](#exporting-youtube-cookies---overview)
    - [Get cookies from browser](#get-cookies-from-browser)
    - [Convert cookies into netscape format](#convert-cookies-into-netscape-format)
  - [Environment Setup](#environment-setup)
  - [Script Usage](#script-usage)
  - [How to upload downloaded content to your smartphone?](#how-to-upload-downloaded-content-to-your-smartphone)
  - [Update yt-dlp](#update-yt-dlp)
  - [Audio Quality Guide](#audio-quality-guide)


## Manage Cookies

### Exporting YouTube cookies - Overview

Source: https://github.com/yt-dlp/yt-dlp/wiki/Extractors#exporting-youtube-cookies

One way to do this is through a private browsing/incognito window:

- Open a new private browsing/incognito window and log into YouTube
- In same window and same tab from step 1, navigate to https://www.youtube.com/robots.txt (this should be the only private/incognito browsing tab open)
- Export youtube.com cookies from the browser, then close the private browsing/incognito window so that the session is never opened in the browser again.

### Get cookies from browser

- Open Dev Tools (F12)
- Application Tab
- In left panel menu choose: Storage \ Cookies \ https://youtube.com
- Ctrl+A (select all), Right click, Copy
- Save it into cookies-chrome.txt file

### Convert cookies into netscape format

`python netscape.py`

## Environment Setup

```bash
source ./venv/bin/activate
pip install requirements.txt
```

## Script Usage

```bash
./loop.sh $id1 $id2 ...
```

## How to upload downloaded content to your smartphone?

https://toffeeshare.com/

Share files directly from your device to anywhere
Send files of any size directly from your device without ever storing anything online.

- No file size limit
- Peer-to-peer
- Blazingly fast
- End-to-end encrypted

## Update yt-dlp

`python3 -m pip install -U "yt-dlp[default]"`

## Audio Quality Guide

32 kbps, mono - minimally acceptable. Speech is intelligible, but may sound "metallic" and become tiring during long listening sessions. Suitable for saving storage space.

48-64 kbps, mono - the optimal balance. Clear speech, small file size (about 25-30 MB per hour). This is the standard for many audiobooks and podcasts.

96 kbps, mono or stereo - comfortable quality. Clean sound, suitable for hours of listening without fatigue. Files are roughly twice the size compared to 48 kbps.

128 kbps, stereo - excessive for audiobooks, but appropriate if music or sound effects are present.
