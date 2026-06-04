test = {
  'name': 'filter_odd',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define t1 (tree 3 (list (tree 4 (list (tree 5 nil))) (tree 7 (list (tree 9 nil))) (tree 1 (list (tree 6 nil))))))
          t1
          scm> (label t1)
          3
          scm> (label (car (branches t1)))
          4
          scm> (define t2 (filter-odd t1))
          t2
          scm> (label t2)
          3
          scm> (label (car (branches t2)))
          ()
          scm> (label (car (branches (car (branches t2)))))
          5
          scm> (label (car (cdr (branches t2))))
          7
          scm> (label (car (branches (car (cdr (branches t2))))))
          9
          scm> (label (car (cdr (cdr (branches t2)))))
          1
          scm> (label (car (branches (car (cdr (cdr (branches t2)))))))
          ()
          """,
          'hidden': False,
          'locked': False,
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
