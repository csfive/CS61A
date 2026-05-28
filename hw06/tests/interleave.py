test = {
  'name': 'interleave',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (interleave (list 1 3 5) (list 2 4))
          007a74414c5bf8168adabc76cf2a1092
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave (list 2 4) (list 1 3 5))
          b28d65653a4ffceb2e6bca28ac7d7107
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave (list 1 2) (list 1 2))
          33064f1a348785cc92e1d4f0f0a21d3d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave '(1 2 3 4 5 6) '(7 8))
          4efca6c54cb5b317b9dc079c3da7a638
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
          scm> (interleave (list 1 3 5) (list 2 4 6))
          06bff4289ef1f36fade4fc6f3f73cbd7
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave (list 1 3 5) nil)
          4cc9884dfb545fbb2d98f3843fec6a4a
          # locked
          scm> (interleave nil (list 1 3 5))
          4cc9884dfb545fbb2d98f3843fec6a4a
          # locked
          scm> (interleave nil nil)
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
