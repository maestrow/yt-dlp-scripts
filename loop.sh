#!/usr/bin/env bash

# List of video IDs
videos=("$@")

# Loop through each video
for video in "${videos[@]}"; do
  echo "Downloading: $video"
  # yt-dlp --cookies cookies.txt -x --audio-format mp3 --audio-quality 16K -k "https://www.youtube.com/watch?v=$video"
  # yt-dlp --cookies cookies.txt -x --audio-format mp3 --audio-quality 16K -k "https://www.youtube.com/watch?v=$video"
  # yt-dlp --cookies cookies.txt "https://www.youtube.com/watch?v=$video"
  yt-dlp --cookies cookies.txt -x --audio-format mp3 --postprocessor-args "-ac 1 -ar 22050 -b:a 32k" "https://www.youtube.com/watch?v=$video"

  echo "-----------------------------------"
done
