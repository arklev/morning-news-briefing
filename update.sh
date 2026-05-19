#!/bin/bash
cd ~/morning_briefing
echo 'Updating code from GitHub...'
git pull origin main
echo 'Syncing dependencies...'
venv/bin/pip install -r requirements.txt
echo 'Update complete.'
