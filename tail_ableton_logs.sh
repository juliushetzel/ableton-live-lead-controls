LATEST_VERSION_PATH=$(ls -1dt $HOME/Library/Preferences/Ableton/Live* | head -n 1)
echo "Tailing $LATEST_VERSION_PATH"
tail -f "$LATEST_VERSION_PATH/Log.txt"