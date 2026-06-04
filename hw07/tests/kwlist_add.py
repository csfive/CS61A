test = {
  'name': 'kwlist-add',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define ex-lst (make-kwlist '(a b c) '(1 2 3)))
          ex-lst
          scm> (get-keys-kwlist ex-lst)
          (a b c)
          scm> (get-values-kwlist ex-lst)
          (1 2 3)
          scm> (define ex-lst (add-to-kwlist ex-lst 'd '4))
          ex-lst
          scm> (get-keys-kwlist ex-lst) ; note that new items are at the end of the list!
          (a b c d)
          scm> (get-values-kwlist ex-lst) ; here too!
          (1 2 3 4)
          scm> (define ex-lst (add-to-kwlist ex-lst 'e '1))
          ex-lst
          scm> (get-keys-kwlist ex-lst) ; duplicate keys are okay!
          (a b c d e)
          scm> (get-values-kwlist ex-lst)
          (1 2 3 4 1)
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
          scm> (get-keys-kwlist ex-lst)
          (a b c)
          scm> (get-values-kwlist ex-lst)
          (1 2 3)
          scm> (define ex-lst (add-to-kwlist ex-lst 'd '4))
          ex-lst
          scm> (get-keys-kwlist ex-lst) ; note that new items are at the end of the list!
          (a b c d)
          scm> (get-values-kwlist ex-lst) ; here too!
          (1 2 3 4)
          scm> (define ex-lst (add-to-kwlist ex-lst 'e '1))
          ex-lst
          scm> (get-keys-kwlist ex-lst) ; duplicate keys are okay!
          (a b c d e)
          scm> (get-values-kwlist ex-lst)
          (1 2 3 4 1)
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
