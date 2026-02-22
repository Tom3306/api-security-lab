#!/usr/bin/env bash
set -euo pipefail

echo "[+] Running OWASP ZAP baseline scan against http://localhost:8000"
docker run --rm -t \
  -v "$(pwd):/zap/wrk:rw" \
  ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py -t http://host.docker.internal:8000 -r zap-report.html

echo "[+] Report generated: ./zap-report.html"
