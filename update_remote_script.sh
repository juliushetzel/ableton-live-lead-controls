REPOSITORY_DIR="$(dirname "$0")"
REMOTE_SCRIPTS_PATH="$HOME/Music/Ableton/User Library/Remote Scripts"
rm -R "$REMOTE_SCRIPTS_PATH/LeadControl"
cp -R "$REPOSITORY_DIR/src/lead_control" "$REMOTE_SCRIPTS_PATH/LeadControl"