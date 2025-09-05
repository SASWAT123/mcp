#!/bin/bash
set -e

echo "Installing uv..."
pip install uv

echo "Creating virtual environment..."
uv venv

echo "Installing dependencies..."
source .venv/bin/activate
uv pip install openai pytest ruff mypy pydantic

echo "Post-create setup complete!"