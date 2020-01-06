#!/bin/bash

echo "kill django if open on 8000"
kill -9 $(lsof -Pnl +M -i | grep 8000 | awk '{print $2}')

