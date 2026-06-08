from scheme_builtins import *
from scheme_classes import *
from scheme_eval_apply import *
from scheme_utils import *

#################
# Special Forms #
#################

"""
How you implement special forms is up to you. We recommend you encapsulate the
logic for each special form separately somehow, which you can do here.
"""


# BEGIN PROBLEM 2/3
def do_define_form(expressions, env):
    """Evaluate a define form."""
    validate_form(expressions, 2)
    signature = expressions.first
    if scheme_symbolp(signature):
        validate_form(expressions, 2, 2)
        value = scheme_eval(expressions.rest.first, env)
        env.define(signature, value)
        return signature
    elif isinstance(signature, Pair) and scheme_symbolp(signature.first):
        name = signature.first
        formals = signature.rest
        validate_formals(formals)
        procedure = LambdaProcedure(formals, expressions.rest, env)
        env.define(name, procedure)
        return name
    else:
        bad_signature = signature.first if isinstance(signature, Pair) else signature
        raise SchemeError("non-symbol: {0}".format(bad_signature))


def do_quote_form(expressions, env):
    """Evaluate a quote form."""
    validate_form(expressions, 1, 1)
    return expressions.first


def do_begin_form(expressions, env):
    """Evaluate a begin form."""
    validate_form(expressions, 1)
    return eval_all(expressions, env)


def do_lambda_form(expressions, env):
    """Evaluate a lambda form."""
    validate_form(expressions, 2)
    formals = expressions.first
    validate_formals(formals)
    return LambdaProcedure(formals, expressions.rest, env)


def do_if_form(expressions, env):
    """Evaluate an if form."""
    validate_form(expressions, 2, 3)
    if is_scheme_true(scheme_eval(expressions.first, env)):
        return scheme_eval(expressions.rest.first, env, True)
    elif len(expressions) == 3:
        return scheme_eval(expressions.rest.rest.first, env, True)


def do_and_form(expressions, env):
    """Evaluate a short-circuited and form."""
    result = True
    while expressions is not nil:
        if expressions.rest is nil:
            return scheme_eval(expressions.first, env, True)
        result = scheme_eval(expressions.first, env)
        if is_scheme_false(result):
            return result
        expressions = expressions.rest
    return result


def do_or_form(expressions, env):
    """Evaluate a short-circuited or form."""
    result = False
    while expressions is not nil:
        if expressions.rest is nil:
            return scheme_eval(expressions.first, env, True)
        result = scheme_eval(expressions.first, env)
        if is_scheme_true(result):
            return result
        expressions = expressions.rest
    return result


def do_cond_form(expressions, env):
    """Evaluate a cond form."""
    while expressions is not nil:
        clause = expressions.first
        validate_form(clause, 1)
        if clause.first == "else":
            test = True
            if expressions.rest is not nil:
                raise SchemeError("else must be last")
        else:
            test = scheme_eval(clause.first, env)
        if is_scheme_true(test):
            if clause.rest is nil:
                return test
            return eval_all(clause.rest, env)
        expressions = expressions.rest


def make_let_frame(bindings, env):
    """Create a child frame for let bindings."""
    if not scheme_listp(bindings):
        raise SchemeError("bad bindings list in let form")
    names = vals = nil
    while bindings is not nil:
        binding = bindings.first
        validate_form(binding, 2, 2)
        name = binding.first
        value = scheme_eval(binding.rest.first, env)
        names = Pair(name, names)
        vals = Pair(value, vals)
        bindings = bindings.rest
    validate_formals(names)
    return env.make_child_frame(names, vals)


def do_let_form(expressions, env):
    """Evaluate a let form."""
    validate_form(expressions, 2)
    let_env = make_let_frame(expressions.first, env)
    return eval_all(expressions.rest, let_env)


def do_mu_form(expressions, env):
    """Evaluate a mu form."""
    validate_form(expressions, 2)
    formals = expressions.first
    validate_formals(formals)
    return MuProcedure(formals, expressions.rest)


def do_define_macro(expressions, env):
    """Evaluate a define-macro form."""
    validate_form(expressions, 2)
    signature = expressions.first
    if not isinstance(signature, Pair) or not scheme_symbolp(signature.first):
        raise SchemeError("invalid macro signature")
    name = signature.first
    formals = signature.rest
    validate_formals(formals)
    procedure = MacroProcedure(formals, expressions.rest, env)
    env.define(name, procedure)
    return name


def do_quasiquote_form(expressions, env):
    """Evaluate a quasiquote form."""

    def quasiquote_item(val, env, level):
        if not scheme_pairp(val):
            return val

        if scheme_symbolp(val.first) and val.first == "unquote":
            level -= 1
            if level == 0:
                expressions = val.rest
                validate_form(expressions, 1, 1)
                return scheme_eval(expressions.first, env)
        elif val.first == "quasiquote":
            level += 1

        return val.map(lambda elem: quasiquote_item(elem, env, level))

    validate_form(expressions, 1, 1)
    return quasiquote_item(expressions.first, env, 1)


def do_unquote(expressions, env):
    raise SchemeError("unquote outside of quasiquote")


SPECIAL_FORMS = {
    "and": do_and_form,
    "begin": do_begin_form,
    "cond": do_cond_form,
    "define": do_define_form,
    "if": do_if_form,
    "lambda": do_lambda_form,
    "let": do_let_form,
    "or": do_or_form,
    "quote": do_quote_form,
    "define-macro": do_define_macro,
    "quasiquote": do_quasiquote_form,
    "unquote": do_unquote,
    "mu": do_mu_form,
}
# END PROBLEM 2/3
