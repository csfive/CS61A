test = {
  'name': 'What Would Scheme Display?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define x (rational 2 5))
          ecf2b304041c91c68610920edf6214eb
          # locked
          scm> (numer x)
          b764c5386326cd8ae89e4efe0c923e84
          # locked
          scm> (denom x)
          3b2d9316bebaa3b3f233e455d255a9e1
          # locked
          scm> (define y (rational 1 4))
          87e09802e0243f4d9aa26908b733336c
          # locked
          scm> (define z1 (add-rational x y))
          32eb0b0bab5709764f7684e503498151
          # locked
          scm> (numer z1)
          d7c7eb47da54a13f980493ac7d8b9b65
          # locked
          scm> (denom z1)
          f9ff38eeedff271ae8c1da1dd024b2ec
          # locked
          scm> (define z2 (mul-rational x y))
          3bc71d780e6b21e0abd53fbffcb24bd2
          # locked
          scm> (numer z2)
          f313ff1ce5644f8b5465a3f45b4f19a4
          # locked
          scm> (denom z2)
          ff2443dd373fbd084719804738d09b80
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define t (tree 1 (list (tree 2 nil))))
          39acca2d57ab183dd99453a5334d67d5
          # locked
          scm> (label t)
          f313ff1ce5644f8b5465a3f45b4f19a4
          # locked
          scm> (length (branches t))
          f313ff1ce5644f8b5465a3f45b4f19a4
          # locked
          scm> (define child (car (branches t)))
          1deb9adcb2e2af283609ea135533bf8b
          # locked
          scm> (label child)
          b764c5386326cd8ae89e4efe0c923e84
          # locked
          scm> (is-leaf child)
          309b33224b9a47888ae45fc6e19fa6e6
          # locked
          scm> (branches child)
          afed03a4bad4b019a15373c410ea3792
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define b1 (tree 5 (list (tree 6 nil) (tree 7 nil)) )) 
          8b3cdc93a1a6616cbeb588569b2d5c80
          # locked
          scm> (map is-leaf (branches b1))  ; draw the tree if you get stuck!
          cf2835b345e001ebb561ae95c23d30e3
          # locked
          scm> (define b2 (tree 8 (list (tree 9 (list (tree 10 nil)) )) )) 
          efa3f8d62df45591d10f7f251966583f
          # locked
          scm> (map is-leaf (branches b2))  ; draw the tree if you get stuck!
          8297350b7fdb18a1dbdb44e47abeadde
          # locked
          scm> (define t (tree 11 (list b1 b2)))
          39acca2d57ab183dd99453a5334d67d5
          # locked
          scm> (label t)
          28ee5399d75ef3bec6592a11a761594f
          # locked
          scm> (map (lambda (b) (label b)) (branches t))
          5e6e197c7088e8b03fe7bdd26aa1d738
          # locked
          """,
          'hidden': False,
          'locked': True,
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
