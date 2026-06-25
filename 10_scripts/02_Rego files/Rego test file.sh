#!/bin/bash
echo "========================================="
echo "Multi-Domain Trust Algorithm - Rego Test"
echo "========================================="

# Load policy into OPA
echo "Loading policy into OPA..."
curl -X PUT http://localhost:8182/v1/policies/trust-algorithm \
  -H "Content-Type: text/plain" \
  --data-binary @trust_algorithm.rego

# Test scenarios
echo -e "\n\n--- SCENARIO 1: HIGH TRUST ---"
curl -s -X POST http://localhost:8182/v1/data/zero_trust/trust_algorithm/decision \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
        "data": {"integrity": 0.95, "freshness": 0.92, "authenticity": 0.98, "confidence": 1.0},
        "device": {"identity": 0.98, "reputation": 0.90, "compliance": 0.95, "confidence": 0.95},
        "application": {"vulnerability": 0.85, "consistency": 0.92, "access_compliance": 0.94, "confidence": 0.90},
        "network": {"anomalies": 0.97, "protocol_score": 0.96, "node_reputation": 0.92, "confidence": 0.95}
    }
}' | jq '.result'

echo -e "\n\n--- SCENARIO 2: MEDIUM TRUST ---"
curl -s -X POST http://localhost:8182/v1/data/zero_trust/trust_algorithm/decision \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
        "data": {"integrity": 0.70, "freshness": 0.65, "authenticity": 0.68, "confidence": 0.80},
        "device": {"identity": 0.60, "reputation": 0.55, "compliance": 0.62, "confidence": 0.70},
        "application": {"vulnerability": 0.58, "consistency": 0.64, "access_compliance": 0.66, "confidence": 0.75},
        "network": {"anomalies": 0.72, "protocol_score": 0.68, "node_reputation": 0.70, "confidence": 0.80}
    }
}' | jq '.result'

echo -e "\n\n--- SCENARIO 3: LOW TRUST ---"
curl -s -X POST http://localhost:8182/v1/data/zero_trust/trust_algorithm/decision \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
        "data": {"integrity": 0.30, "freshness": 0.25, "authenticity": 0.28, "confidence": 0.50},
        "device": {"identity": 0.35, "reputation": 0.30, "compliance": 0.25, "confidence": 0.40},
        "application": {"vulnerability": 0.25, "consistency": 0.35, "access_compliance": 0.30, "confidence": 0.45},
        "network": {"anomalies": 0.30, "protocol_score": 0.40, "node_reputation": 0.35, "confidence": 0.50}
    }
}' | jq '.result'

echo -e "\n\n--- SCENARIO 4: HIGH UNCERTAINTY ---"
curl -s -X POST http://localhost:8182/v1/data/zero_trust/trust_algorithm/decision \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
        "data": {"integrity": 0.0, "freshness": 0.0, "authenticity": 0.0, "confidence": 0.20},
        "device": {"identity": 0.75, "reputation": 0.0, "compliance": 0.0, "confidence": 0.35},
        "application": {"vulnerability": 0.0, "consistency": 0.0, "access_compliance": 0.0, "confidence": 0.15},
        "network": {"anomalies": 0.60, "protocol_score": 0.0, "node_reputation": 0.0, "confidence": 0.25}
    }
}' | jq '.result'