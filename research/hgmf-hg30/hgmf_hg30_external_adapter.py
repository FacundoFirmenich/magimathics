#!/usr/bin/env python3
from __future__ import annotations

def validate_bounded_process_tensor_spec(spec):
    required=("memory_steps","local_dimension","bond_dimension_cap","tomography_algorithm","training_only","holdout_wave")
    missing=[k for k in required if k not in spec]
    if missing: raise ValueError("missing PT cap: "+",".join(missing))
    if spec["memory_steps"]<1 or spec["local_dimension"]<2 or spec["bond_dimension_cap"]<1:
        raise ValueError("invalid PT complexity cap")
    if spec["training_only"] is not True or spec["holdout_wave"]!=3:
        raise ValueError("PT split violation")
    return {"status":"INTERFACE_VALID","confirmatory_calibration":"REQUIRES_ENGINE_SPECIFIC_PROOF_OR_VALIDATED_SPLIT_CHECK"}

def validate_ancilla_geometry_spec(spec):
    required=("latent_dimension_cap","map_family","regularization","training_only","holdout_wave")
    missing=[k for k in required if k not in spec]
    if missing: raise ValueError("missing ancilla cap: "+",".join(missing))
    if spec["latent_dimension_cap"]<1: raise ValueError("invalid latent cap")
    if spec["training_only"] is not True or spec["holdout_wave"]!=3:
        raise ValueError("ancilla split violation")
    return {"status":"INTERFACE_VALID","confirmatory_calibration":"REQUIRES_ENGINE_SPECIFIC_PROOF_OR_VALIDATED_SPLIT_CHECK"}
