LATEST_VERSION_PATH=$(ls -1dt $HOME/Library/Preferences/Ableton/Live* | head -n 1)
tail -f "$LATEST_VERSION_PATH/Log.txt"