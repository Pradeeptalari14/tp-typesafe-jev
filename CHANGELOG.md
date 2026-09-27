# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-09-27

### Added
- Initial release of TypeSafe Jev System 1 Decision Studio repository (`tp-typesafe-jev`).
- Non-autoregressive sub-100ms Python client using Pydantic v2 schemas (`primary_config/jev_client.py`).
- Fastify/Express TypeScript router middleware with Zod v3 validation (`primary_config/system1_router.ts`).
- Dual-Process LangGraph state graph with dynamic confidence-gated cognitive routing (`primary_config/hybrid_agent_graph.py`).
- Production Kubernetes Pod deployment manifest with Jev local gRPC inference sidecar container (`primary_config/k8s-jev-sidecar.yaml`).
- SRE architecture topology diagrams and operational validation script (`scripts/validate.sh`).
