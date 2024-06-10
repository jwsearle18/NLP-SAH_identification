#!/bin/bash

# Check if a pattern was provided
if [ -z "$1" ]; then
  echo "Usage: $0 <pattern>"
  exit 1
fi

# Assign the pattern from the first argument
pattern="$1"

# Directory containing the tar files
directory="."

# Loop through each tar file in the directory
for archive in "$directory"/*.tar; do
  echo "Processing $archive..."

  # Create a temporary directory
  tmp_dir=$(mktemp -d)

  # Extract the tar archive into the temporary directory
  tar -xzf "$archive" -C "$tmp_dir"

  # Grep through the extracted files
  grep -rH "$pattern" "$tmp_dir"

  # Clean up the temporary directory
  rm -rf "$tmp_dir"
done
