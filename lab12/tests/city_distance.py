test = {
  'name': 'city_distance',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define city-a (make-city 'city-a 0 1))
          city-a
          scm> (define city-b (make-city 'city-b 0 2))
          city-b
          scm> (distance city-a city-b) 
          1.0
          scm> (define city-c (make-city 'city-c 6.5 12))
          city-c
          scm> (define city-d (make-city 'city-d 2.5 15))
          city-d
          scm> (distance city-c city-d) 
          5.0
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
          scm> (define city-a (make-city 'city-a 0 1))
          city-a
          scm> (define city-b (make-city 'city-b 0 2))
          city-b
          scm> (distance city-a city-b) 
          1.0
          scm> (define city-c (make-city 'city-c 6.5 12))
          city-c
          scm> (define city-d (make-city 'city-d 2.5 15))
          city-d
          scm> (distance city-c city-d) 
          5.0
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
