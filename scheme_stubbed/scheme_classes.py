from pair import *


class SchemeError(Exception):
    """Exception indicating an error in a Scheme program."""


################
# Environments #
################


class Frame:
    """An environment frame binds Scheme symbols to Scheme values."""

    def __init__(self, parent):
        """An empty frame with parent frame PARENT (which may be None)."""
        # BEGIN Problem 1
        self.bindings = {}
        self.parent = parent
        # END Problem 1

    def __repr__(self):
        if self.parent is None:
            return "<Global Frame>"
        s = sorted(["{0}: {1}".format(k, v) for k, v in self.bindings.items()])
        return "<{{{0}}} -> {1}>".format(", ".join(s), repr(self.parent))

    def define(self, symbol, value):
        """Define Scheme SYMBOL to have VALUE."""
        # BEGIN Problem 1
        self.bindings[symbol] = value
        # END Problem 1

    # BEGIN Problem 1
    def lookup(self, symbol):
        """Return the value bound to SYMBOL. Errors if SYMBOL is not found."""
        if symbol in self.bindings:
            return self.bindings[symbol]
        elif self.parent is not None:
            return self.parent.lookup(symbol)
        raise SchemeError("unknown identifier: {0}".format(symbol))

    def make_child_frame(self, formals, vals):
        """Return a new local frame whose parent is SELF, in which the symbols
        in a Scheme list of formal parameters FORMALS are bound to the Scheme
        values in the Scheme list VALS."""
        if len(formals) != len(vals):
            raise SchemeError("Incorrect number of arguments to function call")
        frame = Frame(self)
        while formals is not nil:
            frame.define(formals.first, vals.first)
            formals = formals.rest
            vals = vals.rest
        return frame

    # END Problem 1


##############
# Procedures #
##############


class Procedure:
    """The the base class for all Procedure classes."""


class BuiltinProcedure(Procedure):
    """A Scheme procedure defined as a Python function."""

    def __init__(self, py_func, expect_env=False, name="builtin"):
        self.name = name
        self.py_func = py_func
        self.expect_env = expect_env

    def __str__(self):
        return "#[{0}]".format(self.name)


class LambdaProcedure(Procedure):
    """A procedure defined by a lambda expression or a define form."""

    name = "[lambda]"  # Error tracing extension

    def __init__(self, formals, body, env):
        """A procedure with formal parameter list FORMALS (a Scheme list),
        whose body is the Scheme list BODY, and whose parent environment
        starts with Frame ENV."""
        assert isinstance(env, Frame), "env must be of type Frame"

        from scheme_utils import scheme_listp, validate_type

        validate_type(formals, scheme_listp, 0, "LambdaProcedure")
        validate_type(body, scheme_listp, 1, "LambdaProcedure")
        self.formals = formals
        self.body = body
        self.env = env

    def __str__(self):
        return str(Pair("lambda", Pair(self.formals, self.body)))

    def __repr__(self):
        return "LambdaProcedure({0}, {1}, {2})".format(
            repr(self.formals), repr(self.body), repr(self.env)
        )


class MacroProcedure(LambdaProcedure):
    """A macro procedure."""


class MuProcedure(Procedure):
    """A procedure defined by a mu expression, which has dynamic scope.
     _________________
    < Scheme is cool! >
     -----------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
    """

    name = "[mu]"  # Error tracing extension

    def __init__(self, formals, body):
        """A procedure with formal parameter list FORMALS (a Scheme list) and
        Scheme list BODY as its definition."""
        self.formals = formals
        self.body = body

    def __str__(self):
        return str(Pair("mu", Pair(self.formals, self.body)))

    def __repr__(self):
        return "MuProcedure({0}, {1})".format(repr(self.formals), repr(self.body))
