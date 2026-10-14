#!/bin/bash
cd "$(dirname "$0")/src"
clear
echo "================================================================================="
echo " 🛸 NWO: NEW WORLD ORDER — INITIALIZING SYSTEM LIFECYCLE CONTROLLERS "
echo "================================================================================="
python3 nwo_server_bridge.py &
SERVER_PID=$!
sleep 1
open "ui_launch_menu.html" 2>/dev/null || open "http://localhost:8080"
python3 nwo_core_engine.py
kill $SERVER_PID 2>/dev/null
echo "🔌 System unmounted cleanly."
