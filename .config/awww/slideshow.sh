
#!/usr/bin/env bash

WALLPAPER_DIR="$HOME/Pictures/Wallpapers"
INTERVAL=60

mapfile -d '' wallpapers < <(
    find "$WALLPAPER_DIR" -maxdepth 1 -type f \
        \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' -o -iname '*.webp' \) \
        -print0 | sort -zV
)

while true; do
    for wallpaper in "${wallpapers[@]}"; do
        awww img "$wallpaper" \
            --transition-type fade \
            --transition-duration 2
        sleep "$INTERVAL"
    done
done
