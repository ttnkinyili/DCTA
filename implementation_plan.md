# Implementation Plan - Granular Trust & Hybrid Fusion

We are transitioning from a simple domain-level trust score to a granular parameter-based model. The fusion approach will now be a hybrid of **Dynamic Weighted Sum** (for parameters within a domain) and **Weighted Belief Fusion** (for combining domains).

## Domains & Parameters
1.  **Data**: Integrity, Freshness, Authenticity
2.  **Device**: Identity, Reputation, Compliance
3.  **Application**: Vulnerability Score, Consistency, Access Compliance
4.  **Network**: Anomalies, Protocol Score, Node Reputation

## Proposed Changes

### [Refactor] [dynamic_trust_weighting.py](file:///Users/admin/Desktop/DCTA/dynamic_trust_weighting.py)
- **New Structure**: `TrustSimulator` will generate values (0.0-1.0) for each *parameter* instead of just the domain.
- **Intra-Domain Aggregation (Dynamic Weighted Sum)**:
    - Each parameter will have a weight.
    - $Score_{Domain} = \sum (Value_{param} \times Weight_{param})$
    - This provides the "Raw Trust" for the domain.
- **Inter-Domain Weighting**:
    - We will still calculate the "Contextual Weight" ($W_{ctx}$) of the Domain based on the stability (variance) of its aggregated score.

### [Refactor] [cumulative_belief_fusion.py](file:///Users/admin/Desktop/DCTA/cumulative_belief_fusion.py)
- **Input**: Receives the Aggregated Domain Score and the Contextual Weight ($W_{ctx}$).
- **Weighted Belief Fusion**:
    - Convert Domain Score to Mass Function (Evidence).
    - Discount Evidence using $W_{ctx}$ (Shafer's Discounting):
        - $m_{discounted}(A) = W_{ctx} \times m(A)$
        - $m_{discounted}(\Theta) = 1 - W_{ctx} + W_{ctx} \times m(\Theta)$
    - Fuse discounted masses using Dempster's Rule.

## Verification Plan
- Run the simulation and check if the "Untrusted Device" scenario still behaves correctly (Low Compliance/Reputation -> Low Device Score -> System Uncertainty/Denial).
