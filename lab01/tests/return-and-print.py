test = {
  'name': 'return-and-print',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def welcome():
          ...     print('Go')
          ...     return 'hello'
          >>> def cal():
          ...     print('Bears')
          ...     return 'world'
          >>> welcome()
          Go
          'hello'
          >>> print(welcome(), cal())
          Go
          Bears
          hello world
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
