""" Base class for systems in OpenMDAO."""


class System(object):
    def __init__(self):
        self.name = ''
        # by default, don't promote any vars up to our parent
        self.promotes = ()

        # These point to (du,df) or (df,du) depending on mode.
        # TODO: Since systems don't own their own variables, we might lose
        # the convenience of these.
        self.sol_vec = None
        self.rhs_vec = None

    def promoted(self, name):
        # TODO: handle wildcards
        return name in self.promotes

    def setup_vectors(self, parent_vm=None):
        pass

    def preconditioner(self):
        pass

    def jacobian(self, params, unknowns):
        pass

    def solve_nonlinear(self, params, unknowns, resids):
        pass

    def apply_nonlinear(self, params, unknowns, resids):
        pass

    def solve_linear(self, params, unknowns, resids, dparams, dunknowns,
        dresids, mode="fwd"):
        pass

    def apply_linear(self, params, unknowns, resids, dparams, dunknowns,
        dresids, mode="fwd"):
        pass