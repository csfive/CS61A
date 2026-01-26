test = {
  'name': 'Question 2',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'answer': 'The function mapped to the digit 3',
          'choices': [
            'The function mapped to the digit 1',
            'The function mapped to the digit 2',
            'The function mapped to the digit 3',
            'The function mapped to the digit 5'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': r"""
          The opponent's score is 123. The current player's score is 5.
          Say the current player decides to roll 0 dice on this turn.
          What is the first function applied to the current player's score (5)
          according to Hefty Hogs?
          """
        },
        {
          'answer': 'The function mapped to the digit 2',
          'choices': [
            'The function mapped to the digit 1',
            'The function mapped to the digit 2',
            'The function mapped to the digit 3',
            'The function mapped to the digit 5'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What is the second function applied to the result of the first?'
        },
        {
          'answer': 'The function mapped to the digit 1',
          'choices': [
            'The function mapped to the digit 1',
            'The function mapped to the digit 2',
            'The function mapped to the digit 3',
            'The function mapped to the digit 5'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What is the third function applied to the result of the second?'
        },
        {
          'answer': 'f1( f2( f3(5) )) % 30',
          'choices': [
            'f1( f2( f3(5) ))',
            'f1( f2( f3(5) )) % 30',
            'f3( f2( f1(5) ))',
            'f3( f2( f1(5) )) % 30'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': r"""
          What is the overall result of Hefty Hogs for this turn?
          The opponent's score is 123, and the current player's score is 5.
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> hefty_hogs(5, 123)
          9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(5, 456)
          29
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> a = hefty_hogs(5, 123)
          >>> a # check that the value is being returned, not printed
          9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(3, 12345)
          9
          >>> # ban str and indexing (lists)
          >>> test.check('hog.py', 'hefty_hogs', ['Str', 'Slice', 'List', 'ListComp', 'Index', 'Subscript', 'For'])
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(64, 67)
          24
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(12, 72)
          16
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(72, 22)
          18
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(3, 56)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(439, 709)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(61, 16)
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(99, 84)
          24
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(25, 67)
          24
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(5, 90)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(54, 56)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(15, 64)
          24
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(80, 91)
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(6, 2)
          18
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(74, 16)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(12, 22)
          18
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(12, 5)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(69, 65)
          24
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(15, 6)
          8
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(69, 62)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(98, 40)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(15, 95)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(56, 4)
          21
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(44, 64)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(40, 73)
          28
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(192, 343)
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(90, 15)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(6, 48)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(72, 31)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(5, 22)
          15
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hefty_hogs(34, 40)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
