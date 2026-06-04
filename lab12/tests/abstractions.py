test = {
  'name': 'What Would Scheme Display?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define x (rational 2 5))
          x
          scm> (numer x)
          2
          scm> (denom x)
          5
          scm> (define y (rational 1 4))
          y
          scm> (define z1 (add-rational x y))
          z1
          scm> (numer z1)
          13
          scm> (denom z1)
          20
          scm> (define z2 (mul-rational x y))
          z2
          scm> (numer z2)
          1
          scm> (denom z2)
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define t (tree 1 (list (tree 2 nil))))
          t
          scm> (label t)
          1
          scm> (length (branches t))
          1
          scm> (define child (car (branches t)))
          child
          scm> (label child)
          2
          scm> (is-leaf child)
          #t
          scm> (branches child)
          ()
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define b1 (tree 5 (list (tree 6 nil) (tree 7 nil)) )) 
          b1
          scm> (map is-leaf (branches b1))  ; draw the tree if you get stuck!
          (#t #t)
          scm> (define b2 (tree 8 (list (tree 9 (list (tree 10 nil)) )) )) 
          b2
          scm> (map is-leaf (branches b2))  ; draw the tree if you get stuck!
          (#f)
          scm> (define t (tree 11 (list b1 b2)))
          t
          scm> (label t)
          11
          scm> (map (lambda (b) (label b)) (branches t))
          (5 8)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load "./lab12.scm")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
