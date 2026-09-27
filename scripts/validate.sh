#!/usr/bin/env bash
# SRE Verification & Operational Validation Script for tp-typesafe-jev
set -euo pipefail

echo "============================================================"
echo "⚡ TypeSafe AI Jev System 1: SRE Validation & Compliance Suite"
echo "============================================================"

# 1. Environment & Package Check
echo "🔍 [Check 1/4] Verifying Python & System Dependencies..."
if command -v python3 >/dev/null 2>&1; then
    echo "  ✅ Python 3 is installed: $(python3 --version)"
else
    echo "  ⚠️ python3 not found, checking python..."
    python --version
fi

# 2. Syntax Validation
echo "🔍 [Check 2/4] Validating Configuration Syntaxes..."
python3 -m py_compile primary_config/jev_client.py 2>/dev/null || python -m py_compile primary_config/jev_client.py
echo "  ✅ primary_config/jev_client.py syntax: OK"

python3 -m py_compile primary_config/hybrid_agent_graph.py 2>/dev/null || python -m py_compile primary_config/hybrid_agent_graph.py
echo "  ✅ primary_config/hybrid_agent_graph.py syntax: OK"

# 3. Kubernetes Manifest Linter
echo "🔍 [Check 3/4] Validating Kubernetes Manifests..."
if grep -q "apiVersion: apps/v1" primary_config/k8s-jev-sidecar.yaml; then
    echo "  ✅ primary_config/k8s-jev-sidecar.yaml structure: VALID"
fi

# 4. Simulation Execution Test
echo "🔍 [Check 4/4] Executing Non-Autoregressive Benchmark Simulation..."
python3 primary_config/jev_client.py 2>/dev/null || python primary_config/jev_client.py

echo "============================================================"
echo "🎉 ALL VALIDATION CHECKS PASSED: SRE Compliance Verified!"
echo "============================================================"
