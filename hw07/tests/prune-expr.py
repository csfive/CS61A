test = {
  'name': 'prune-expr',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (prune-expr '(+ 10 20))
          (+ 10)
          scm> (prune-expr '(* 10))
          (* 10)
          scm> (prune-expr '(* 4 5 3 2 10))
          (* 4 3 10)
          scm> (eval (prune-expr '(+ 20 40 60)))
          80
          scm> (eval (prune-expr '(- 100 50 30)))
          70
          scm> (eval (prune-expr '(* 4 5 3 2 10)))
          120
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load "./hw07.scm")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
