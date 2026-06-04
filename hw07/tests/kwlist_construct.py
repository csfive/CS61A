test = {
  'name': 'kwlist-construct',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define ex-lst1 (make-kwlist1 '(a b c) '(1 2 3)))
          ex-lst1
          scm> ex-lst1
          ((a b c) (1 2 3))
          scm> (get-keys-kwlist1 ex-lst1)
          (a b c)
          scm> (get-values-kwlist1 ex-lst1)
          (1 2 3)
          scm> (define ex-lst2 (make-kwlist1 '(d e f) '(4 5 6)))
          ex-lst2
          scm> ex-lst2
          ((d e f) (4 5 6))
          scm> (get-keys-kwlist1 ex-lst2)
          (d e f)
          scm> (get-values-kwlist1 ex-lst2)
          (4 5 6)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define ex-lst1 (make-kwlist2 '(a b c) '(1 2 3)))
          ex-lst1
          scm> ex-lst1
          ((a 1) (b 2) (c 3))
          scm> (get-keys-kwlist2 ex-lst1)
          (a b c)
          scm> (get-values-kwlist2 ex-lst1)
          (1 2 3)
          scm> (define ex-lst2 (make-kwlist2 '(d e f) '(4 5 6)))
          ex-lst2
          scm> ex-lst2
          ((d 4) (e 5) (f 6))
          scm> (get-keys-kwlist2 ex-lst2)
          (d e f)
          scm> (get-values-kwlist2 ex-lst2)
          (4 5 6)
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
