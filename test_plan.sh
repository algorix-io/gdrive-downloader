#!/bin/bash
echo "Starting local PHP server..."
php -S localhost:8000 &
PHP_PID=$!
sleep 2
echo "Running Playwright tests..."
python3 verify_ux.py
kill $PHP_PID
