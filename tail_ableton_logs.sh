tail -f "$HOME/Library/Preferences/Ableton/Live 11.3.35/Log.txt" | awk '
  /error/ {print "\033[31m" $0 "\033[39m"}
  /**/ {print "\033[32m" $0 "\033[39m"}
'