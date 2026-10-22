#!/usr/bin/env python3
"""Optional Session-1 architecture declaration guardrail (stdlib only).
Usage: python 07_Guardrail_CI.py 08_Architecture_Policy.json
Checks declared design policy; it does NOT prove actual runtime enforcement.
"""
import json, sys
from pathlib import Path

REQUIRED = {
    "marketing_consent_check_at_send": True,
    "human_campaign_approval_required": True,
    "ai_can_send_directly": False,
    "pii_allowed_in_llm_prompts": False,
    "daily_batch_scoring": True,
    "customer_transaction_write_access_for_ai": False,
}

def validate(data):
    return [f"{k}: required {v!r}, got {data.get(k, '<MISSING>')!r}"
            for k, v in REQUIRED.items() if data.get(k) is not v]

def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("08_Architecture_Policy.json")
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(config, dict):
            raise ValueError("Architecture policy must be a JSON object")
    except (OSError, ValueError) as e:
        print(f"FAIL: cannot read configuration: {e}")
        return 2
    issues = validate(config)
    if issues:
        print("FAIL: architecture policy violates P1/P2/P4:")
        for item in issues:
            print(" - " + item)
        return 1
    print("PASS: six declared policy requirements present; manual design/runtime review still required.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
