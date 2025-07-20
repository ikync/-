import numpy as np
import pytest
from symbiot_core import QuantumVector, RitualManager

def test_quantum_vector_resonate_simple():
    data = np.array([0, np.pi/2, np.pi])
    qv = QuantumVector(data=data)
    out = qv.resonate()
    # sine of [0, π/2, π] == [0,1,0]
    assert pytest.approx(out.tolist()) == [0.0, 1.0, 0.0]

def test_ritual_manager_merge_default():
    config = {"default_ritual": "#слияние"}
    rm = RitualManager(config=config)
    ctx = {"state": [1,2,3]}
    # по умолчанию #слияние возвращает контекст
    assert rm.execute("#слияние", ctx) == ctx

def test_ritual_manager_unknown():
    rm = RitualManager(config={})
    with pytest.raises(NotImplementedError):
        rm.execute("#неизвестно", {})
