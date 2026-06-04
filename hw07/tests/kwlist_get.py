test = {
  'name': 'kwlist-get',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define ex-lst (make-kwlist '(a b c) '(1 2 3)))
          ex-lst
          scm> (get-first-from-kwlist ex-lst 'b)
          2
          scm> (get-first-from-kwlist ex-lst 'd) ; if not found, return nil
          ()
          scm> (define ex-lst (add-to-kwlist ex-lst 'd '4))
          ex-lst
          scm> (get-first-from-kwlist ex-lst 'b)
          2
          scm> (get-first-from-kwlist ex-lst 'd)
          4
          scm> (define ex-lst (add-to-kwlist ex-lst 'd '5))
          ex-lst
          scm> (get-first-from-kwlist ex-lst 'b)
          2
          scm> (get-first-from-kwlist ex-lst 'd) ; return the *first* occurrence
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".") ; abstraction 1
      scm> (define make-kwlist make-kwlist1)
      scm> (define get-keys-kwlist get-keys-kwlist1)
      scm> (define get-values-kwlist get-values-kwlist1)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define ex-lst (make-kwlist '(a b c) '(1 2 3)))
          ex-lst
          scm> (get-first-from-kwlist ex-lst 'b)
          2
          scm> (get-first-from-kwlist ex-lst 'd) ; if not found, return nil
          ()
          scm> (define ex-lst (add-to-kwlist ex-lst 'd '4))
          ex-lst
          scm> (get-first-from-kwlist ex-lst 'b)
          2
          scm> (get-first-from-kwlist ex-lst 'd)
          4
          scm> (define ex-lst (add-to-kwlist ex-lst 'd '5))
          ex-lst
          scm> (get-first-from-kwlist ex-lst 'b)
          2
          scm> (get-first-from-kwlist ex-lst 'd) ; return the *first* occurrence
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".") ; abstraction 2
      scm> (define make-kwlist make-kwlist2)
      scm> (define get-keys-kwlist get-keys-kwlist2)
      scm> (define get-values-kwlist get-values-kwlist2)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
