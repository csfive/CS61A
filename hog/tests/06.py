test = {
  'name': 'Question 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '88be4ee88e677a5f0781541deb37d1e5',
          'choices': [
            'Nothing (None).',
            'A message.',
            'A player.',
            'The previous leader and a message.',
            'The current leader and a message.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does announce_lead_changes return?'
        },
        {
          'answer': 'b074a55f758d6258f1a67408f2b8ea88',
          'choices': [
            'When the current leader is the same as the previous leader.',
            'When the current leader is different from the previous leader.',
            'After each turn.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          When is the message returned by announce_lead_changes
          not just an empty string?
          """
        },
        {
          'answer': '7245aa58a0e05f5381933ab25fdea59e',
          'choices': [
            'The opponent player of this turn.',
            'The current player of this turn.',
            'The leading player from the previous turn.',
            'The leading player in the current turn.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does the parameter last_leader represent?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # this might not technically be a possible game for the current rules, this shouldn't be relevant
          >>> def wrapper(s0, s1, last_leader=None):
          ...     player, message = announce_lead_changes(s0, s1, last_leader)
          ...     print(player)
          ...     print(message)
          ...     return player
          >>> # Wrapper: calls announce_lead_changes, prints out the return values,
          >>> # and returns the leading player from announce_lead_changes
          >>> leader = wrapper(8, 0)
          0
          Player 0 takes the lead by 8
          >>> leader = wrapper(8, 6, leader) # message is None since no change in leading player
          0
          None
          >>> leader = wrapper(18, 6, leader)
          0
          None
          >>> leader = wrapper(18, 22, leader)
          1
          Player 1 takes the lead by 4
          >>> leader = wrapper(22, 22, leader) # leader is None since the scores are equal
          None
          None
          >>> leader = wrapper(22, 42, leader)
          1
          Player 1 takes the lead by 20
          >>> leader = wrapper(30, 42, leader)
          1
          None
          >>> leader = wrapper(30, 77, leader)
          1
          None
          >>> leader = wrapper(83, 77, leader)
          0
          Player 0 takes the lead by 6
          >>> leader = wrapper(83, 84, leader)
          1
          Player 1 takes the lead by 1
          >>> leader
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import announce_lead_changes
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
