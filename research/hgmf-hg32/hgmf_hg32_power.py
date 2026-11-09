#!/usr/bin/env python3
from __future__ import annotations
import math

def required_log_e(alpha_component=1/140):
    if not 0<alpha_component<1: raise ValueError("alpha")
    return math.log(1/alpha_component)

def required_average_log_advantage(n_holdout:int, slack:float=0.0, alpha_component=1/140):
    if n_holdout<1 or slack<0: raise ValueError("invalid n/slack")
    return (required_log_e(alpha_component)+slack)/n_holdout

def required_holdout_cells(avg_log_advantage:float, slack:float=0.0, alpha_component=1/140):
    if avg_log_advantage<=0 or slack<0: raise ValueError("invalid advantage/slack")
    return math.ceil((required_log_e(alpha_component)+slack)/avg_log_advantage)
