test = {
  'name': 'no-repeats',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (no-repeats '(5 4 3 2 1))
          25d8d27451790f17b99671a6f9953d39
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats '(5 4 3 2 1 1))
          25d8d27451790f17b99671a6f9953d39
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats '(5 5 4 3 2 1))
          25d8d27451790f17b99671a6f9953d39
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats '(12))
          94538726eaaa31f35b21ffd6840890cb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats '(1 1 1 1 1 1))
          e7b3891c5a7d2f503188f1818ec702da
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (no-repeats (list 5 4 2))
          170ffebdc7f915c38c8aa15d87f696ae
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (no-repeats (list 5 4 5 4 2 2))
          170ffebdc7f915c38c8aa15d87f696ae
          # locked
          scm> (no-repeats (list 5 5 5 5 5))
          a34738f609498a74df607429424c3fe2
          # locked
          scm> (no-repeats ())
          d17487605f66346bf68b6fb7c92f6257
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
