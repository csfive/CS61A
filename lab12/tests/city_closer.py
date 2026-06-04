test = {
  'name': 'city_closer',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define berkeley (make-city 'berkeley 37.87 112.26))
          berkeley
          scm> (define stanford (make-city 'stanford 34.05 118.25))
          stanford
          scm> (closer-city 38.33 121.44 berkeley stanford)
          stanford
          scm> (closer-city 36.00 110.01 berkeley stanford)
          berkeley
          scm> (define bucharest (make-city 'bucharest 44.43 26.10))
          bucharest
          scm> (define vienna (make-city 'vienna 48.20 16.37))
          vienna
          scm> (closer-city 41.29 174.78 bucharest vienna)
          bucharest
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
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define berkeley (make-city 'berkeley 37.87 112.26))
          berkeley
          scm> (define stanford (make-city 'stanford 34.05 118.25))
          stanford
          scm> (closer-city 38.33 121.44 berkeley stanford)
          stanford
          scm> (closer-city 36.00 110.01 berkeley stanford)
          berkeley
          scm> (define bucharest (make-city 'bucharest 44.43 26.10))
          bucharest
          scm> (define vienna (make-city 'vienna 48.20 16.37))
          vienna
          scm> (closer-city 41.29 174.78 bucharest vienna)
          bucharest
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load "./lab12.scm")
      scm> (load "./tests/alternate_city.scm") ; abstraction check: load different abstraction!
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
