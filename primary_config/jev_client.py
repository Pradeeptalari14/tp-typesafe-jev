#!/usr/bin/env python3
"""
TypeSafe AI · Jev System 1 Decision Client
Dual-Process Cognitive Architecture: Sub-100ms Non-Autoregressive Decision Engine
Calibrated using Reinforcement Learning for Calibrated Decisions (RLCD)
"""

import os
import time
import asyncio
from typing import Optional, Literal, Dict, Any
from pydantic import BaseModel, Field

# ── Pydantic Schema: High-Speed Agent Reflex Routing ──
class AgentRouterDecision(BaseModel):
    route: Literal["DIRECT_TOOL_CALL", "CACHE_HIT", "ESCALATE_SYSTEM_2"] = Field(
        ..., description="Immediate execution route determined by Jev System 1"
    )
    intent: str = Field(..., description="Normalized intent extracted in a single forward pass")
    target_tool: Optional[str] = Field(None, description="Deterministic microservice or tool slug")
    calibrated_confidence: float = Field(
        ..., ge=0.0, le=1.0, description="RLCD-calibrated decision probability"
    )
    cost_usd: float = Field(0.000078, description="Estimated compute cost for single forward pass")


# ── Dual-Process Orchestrator Class ──
class DualProcessDecisionEngine:
    def __init__(
        self,
        escalation_threshold: float = 0.85,
        latency_sla: str = "85ms",
        calibration_mode: str = "strict_rlcd"
    ):
        self.escalation_threshold = escalation_threshold
        self.latency_sla = latency_sla
        self.calibration_mode = calibration_mode
        self.system2_model_name = "claude-3-7-sonnet"

    async def predict_system1(self, state: Dict[str, Any]) -> AgentRouterDecision:
        """
        Simulated / local gRPC call to TypeSafe AI Jev model.
        In production, binds to unix:///var/run/jev.sock or TypeSafe AI cloud API.
        """
        # Emulate non-autoregressive single matrix forward pass (70ms - 85ms)
        await asyncio.sleep(0.075)
        
        prompt = str(state.get("prompt", "")).lower()
        if "shipping" in prompt or "order" in prompt or "status" in prompt:
            return AgentRouterDecision(
                route="DIRECT_TOOL_CALL",
                intent="order_shipping_inquiry",
                target_tool="shipping-carrier-api",
                calibrated_confidence=0.965,
                cost_usd=0.000078
            )
        else:
            return AgentRouterDecision(
                route="ESCALATE_SYSTEM_2",
                intent="complex_legal_contract_review",
                target_tool=None,
                calibrated_confidence=0.542,
                cost_usd=0.000078
            )

    async def evaluate(self, state: Dict[str, Any]) -> Dict[str, Any]:
        start_ts = time.perf_counter()
        print("⚡ [System 1 · Jev] Initiating non-autoregressive forward pass...")

        decision = await self.predict_system1(state)
        latency_ms = (time.perf_counter() - start_ts) * 1000
        print(f"⚡ [System 1 · Jev] Forward pass finished in {latency_ms:.1f}ms | Confidence: {decision.calibrated_confidence:.3f}")

        # Confidence-Gated Cognitive Routing
        if decision.calibrated_confidence >= self.escalation_threshold:
            print(f"✅ [System 1 Confirmed] Confidence >= {self.escalation_threshold}. Executing immediate reflex action.")
            return {
                "cognitive_layer": "SYSTEM_1_REFLEX",
                "latency_ms": latency_ms,
                "decision": decision.model_dump(),
                "cost_usd": decision.cost_usd
            }
        else:
            print(f"🧠 [Escalating to System 2 · {self.system2_model_name}] Confidence ({decision.calibrated_confidence:.3f}) < {self.escalation_threshold}")
            return await self._escalate_to_system2(state, decision, latency_ms)

    async def _escalate_to_system2(self, state: Dict[str, Any], prior_decision: AgentRouterDecision, prior_latency_ms: float) -> Dict[str, Any]:
        s2_start = time.perf_counter()
        # Simulate invocation of Frontier System 2 deliberative model (Claude 3.7 / GPT-4o)
        await asyncio.sleep(1.8)
        s2_latency = (time.perf_counter() - s2_start) * 1000
        return {
            "cognitive_layer": "SYSTEM_2_DELIBERATION",
            "system2_model": self.system2_model_name,
            "system1_latency_ms": prior_latency_ms,
            "system2_latency_ms": s2_latency,
            "total_latency_ms": prior_latency_ms + s2_latency,
            "decision_payload": prior_decision.model_dump(),
            "cost_usd": 0.012500
        }


if __name__ == "__main__":
    engine = DualProcessDecisionEngine(escalation_threshold=0.85)

    test_ticket = {
        "user_id": "usr_99482",
        "prompt": "What is the status of my order #84920 and expected delivery date?",
        "session_context": {"tier": "enterprise", "history_length": 3}
    }

    print("--- Running Test 1: Immediate System 1 Reflex Query ---")
    res1 = asyncio.run(engine.evaluate(test_ticket))
    print(res1)

    print("\n--- Running Test 2: Ambiguous System 2 Escalation Query ---")
    ambiguous_ticket = {
        "user_id": "usr_99482",
        "prompt": "Review our 15-page SaaS indemnity clause and draft an amendment balancing our mutual liabilities.",
        "session_context": {"tier": "enterprise", "history_length": 12}
    }
    res2 = asyncio.run(engine.evaluate(ambiguous_ticket))
    print(res2)
