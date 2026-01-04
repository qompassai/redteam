#!/usr/bin/env sh
# /qompassai/redteam/scripts/defang.sh
# Qompass AI Sed Defang script
# Copyright (C) 2025 Qompass AI, All rights reserved
# ---------------------------------------------------
#   ./sed-defang.sh input.txt > output.txt
#   ./sed-defang.sh -i input.txt

file="$1"
sed 's/\./[.]/g; s/@/[@]/g; s/http/hxxp/g; s#:\/\/#[:]//#g' "$file"
