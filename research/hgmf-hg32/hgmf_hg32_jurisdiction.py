#!/usr/bin/env python3
from __future__ import annotations

IN="IN_JURISDICTION"
OUT="OUT_OF_JURISDICTION_AS_DISTINCT_NULL"
REDUNDANT="OBSERVATIONALLY_REDUNDANT"
SATURATED="UNFALSIFIABLE_PROJECTION"

def classify(has_observation_map: bool, projection_is_full_simplex: bool=False, dominated_by_existing: bool=False):
    if not has_observation_map:
        return OUT
    if projection_is_full_simplex:
        return SATURATED
    if dominated_by_existing:
        return REDUNDANT
    return IN

def quantum_process_tensor_current_carrier(has_cp_instrument_bridge: bool, has_quantum_outcome_likelihood: bool):
    return classify(has_cp_instrument_bridge and has_quantum_outcome_likelihood)

def require_as_distinct_null(status: str) -> bool:
    return status==IN
