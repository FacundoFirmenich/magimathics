#!/usr/bin/env python3
"""Structural dry-run only. No empirical or synthetic scientific outcomes."""
import numpy as np
from hgmf_hg30_covariance import validate_covariance, propagate_linear
from hgmf_hg30_predictive import minimum_mc_draws
from hgmf_hg30_external_adapter import validate_bounded_process_tensor_spec, validate_ancilla_geometry_spec

def main():
    # Algebraic fixtures only: matrix identities, not experimental outcomes.
    S=np.array([[2.0,0.5],[0.5,1.0]])
    info=validate_covariance(S)
    assert info["rank"]==2
    A=np.array([[1.0,-1.0]])
    Sp=propagate_linear(A,S)
    assert Sp.shape==(1,1) and Sp[0,0]>0
    assert minimum_mc_draws(1/140)==139

    pt=validate_bounded_process_tensor_spec({
      "memory_steps":2,
      "local_dimension":2,
      "bond_dimension_cap":4,
      "tomography_algorithm":"EXTERNAL_FROZEN_ENGINE",
      "training_only":True,
      "holdout_wave":3
    })
    an=validate_ancilla_geometry_spec({
      "latent_dimension_cap":2,
      "map_family":"EXTERNAL_FROZEN_ENGINE",
      "regularization":"FROZEN",
      "training_only":True,
      "holdout_wave":3
    })
    assert pt["status"]=="INTERFACE_VALID"
    assert an["status"]=="INTERFACE_VALID"

    readiness={
      "drift_control":True,
      "alternative_standard_kernels":False,
      "finite_hidden_state":False,
      "bounded_process_tensor":False,
      "hidden_ancilla_control_geometry":False
    }
    assert not all(readiness.values())
    print("PASS_HGMF_HG30_STRUCTURAL_DRYRUN")
    print("empirical_outcomes_generated=false")
    print("covariance_contract=PASS")
    print("minimum_mc_draws_alpha_over_7=139")
    print("process_tensor_interface=PASS")
    print("ancilla_interface=PASS")
    print("nuisance_envelope_confirmatory_ready=false")
    print("expected_X_status=ABSTAIN_NUISANCE_ENVELOPE_INCOMPLETE")

if __name__=="__main__":
    main()
