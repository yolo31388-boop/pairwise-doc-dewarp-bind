import pytest
import imaging.doc_dewarp as mod

CASES = [
    ("surface_mesh_model", (1,)),
    ("curved_line_detect", (1,)),
    ("shadow_adaptive", (1,)),
    ("two_page_split", (1,)),
    ("content_resample", (1,)),
    ("stable_page_order", (1,)),
    ("load_scan", (1,)),
    ("estimate", (1,)),
    ("dewarp", (1,)),
    ("present", (1,)),
    ("validate_dewarp", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
