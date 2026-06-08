import scheme_forms
from pair import *
from scheme_utils import *

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # BEGIN Problem 1/2
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    if not scheme_listp(expr):
        raise SchemeError("malformed list: {0}".format(repl_str(expr)))

    first, rest = expr.first, expr.rest
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)

    procedure = scheme_eval(first, env)
    validate_procedure(procedure)

    if isinstance(procedure, MacroProcedure):
        return scheme_eval(complete_apply(procedure, rest, env), env)

    args = rest.map(lambda operand: scheme_eval(operand, env))
    return scheme_apply(procedure, args, env)
    # END Problem 1/2


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    # BEGIN Problem 1/2
    validate_procedure(procedure)
    if isinstance(procedure, BuiltinProcedure):
        py_args = []
        while args is not nil:
            py_args.append(args.first)
            args = args.rest
        if procedure.expect_env:
            py_args.append(env)
        try:
            return procedure.py_func(*py_args)
        except TypeError:
            raise SchemeError("incorrect number of arguments: {0}".format(procedure))
    elif isinstance(procedure, LambdaProcedure):
        new_env = procedure.env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, new_env)
    elif isinstance(procedure, MuProcedure):
        new_env = env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, new_env)
    else:
        assert False, "Unexpected procedure: {}".format(procedure)
    # END Problem 1/2


def eval_all(expressions, env):
    """Evaluate each expression in EXPRESSIONS and return the last value."""
    result = None
    while expressions is not nil:
        if expressions.rest is nil:
            return scheme_eval(expressions.first, env, True)
        result = scheme_eval(expressions.first, env)
        expressions = expressions.rest
    return result


##################
# Tail Recursion #
##################


# Make classes/functions for creating tail recursive programs here!
# BEGIN Problem EC 1
class Unevaluated:
    """An expression and an environment in which to evaluate it."""

    def __init__(self, expr, env):
        self.expr = expr
        self.env = env


def optimize_tail_calls(unoptimized_scheme_eval):
    """Return a properly tail-recursive version of an eval function."""

    def optimized_eval(expr, env, tail=False):
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)

        result = Unevaluated(expr, env)
        while isinstance(result, Unevaluated):
            result = unoptimized_scheme_eval(result.expr, result.env)
        return result

    return optimized_eval


# END Problem EC 1


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not Unevaluated.
    Right now it just calls scheme_apply, but you will need to change this
    if you attempt the extra credit."""
    validate_procedure(procedure)
    # BEGIN
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    return val
    # END


scheme_eval = optimize_tail_calls(scheme_eval)
