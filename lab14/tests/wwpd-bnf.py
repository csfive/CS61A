test = {
  'name': 'ebnf-pycombinator',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '67b5ff15ca924eb2fdb21d8ab7d04c35',
          'choices': [
            'add(1, 2)',
            'sub(3, 4)',
            'add(sub(1, 2))',
            'add()'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which of the following expressions would NOT be parsable according to this BNF?'
        },
        {
          'answer': '08576e9d55d42841148d20830d3abc78',
          'choices': [
            'add(a, b)',
            'add("a", "b")',
            'add(10, 20)',
            'All of these'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which of these expressions WOULD be parsable according to this BNF?'
        },
        {
          'answer': '2926c41689d520aa46c523fc7c6a81de',
          'choices': [
            'pycomb_call: func "(" arg ("," arg)* ")"',
            'arg: pycomb_call | NUMBER',
            'func: FUNCNAME',
            'FUNCNAME: "add" | "mul" | "sub"'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What line of the BNF should we modify to add support for a "div" operation?'
        },
        {
          'answer': 'baf64f82fe30f0af0d0a42db52fc0f2a',
          'choices': [
            'pycomb_call',
            'arg',
            'func',
            'FUNCNAME',
            'NUMBER',
            'both FUNCNAME and NUMBER',
            'All of these'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which of the following are considered a terminal?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
