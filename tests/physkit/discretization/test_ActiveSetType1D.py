from physkit.discretization.grid_1d import ActiveSetType1D


def test__ActiveSetType1D__members_exist():
    assert ActiveSetType1D.ALL is not None
    assert ActiveSetType1D.INTERIOR is not None
    assert ActiveSetType1D.LEFT_CLOSED is not None
    assert ActiveSetType1D.RIGHT_CLOSED is not None
    assert ActiveSetType1D.LEFT_BOUNDARY is not None
    assert ActiveSetType1D.RIGHT_BOUNDARY is not None
    assert ActiveSetType1D.BOUNDARY is not None


def test__ActiveSetType1D__members_are_unique():
    assert ActiveSetType1D.ALL is ActiveSetType1D.ALL
    assert ActiveSetType1D.ALL is not ActiveSetType1D.INTERIOR
