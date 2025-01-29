#!/bin/bash

echo "generating config.json" && \
echo "........................." && \
envsubst < config.json.template > config.json && \
echo "starting mcp_bridge........." && \
uv run python mcp_bridge/main.py