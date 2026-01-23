test = {
  'name': 'Question 7',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '6d36cf85dceafad42b3816d0df5734e3',
          'choices': [
            'A message.',
            'A player.',
            'A message and a player (in that order).',
            'A player and a message (in that order).'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does a commentary function return?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(5, 6, 5), goal=10, say=announce_lead_changes)
          Player 0 takes the lead by 5
          Player 1 takes the lead by 1
          Player 0 takes the lead by 4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(1), always_roll(2), dice=make_test_dice(1, 3, 3), goal=10, say=announce_lead_changes)
          Player 0 takes the lead by 1
          Player 1 takes the lead by 5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1, player=None):
          ...     return player, f"{s0} {s1}" # message of the form: "s0 s1"
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=5, say=echo)
          d7882c94106188a2f424c5383b507923
          072ed6d8c8b94db1f2452887d165717d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> def count(n):
          ...     def say(s0, s1, curr_count=None):
          ...         if curr_count is None:
          ...           curr_count = n
          ...         return curr_count + 1, str(curr_count) + " " + str(s0)
          ...     return say
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(5), goal=15, say=count(1))
          61f188e55077f84722da3594df10f844
          072a7e5a36da4da6069d77fa89868297
          92aad6b5ebfdcdc3f09c28a51c2b7374
          1ebc4dec05cd236c7d1cbd3262366e5c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, announce_lead_changes
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1, player=None):
          ...     return player, str(s0) + " " + str(s1)
          >>> strat0 = lambda score, opponent: 1 - opponent // 10
          >>> strat1 = always_roll(3)
          >>> s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)
          f4d41f4e29a08f003e0a9a5473c61d5e
          461ff541bd06a2e3310447d10cc6615b
          531055843f87deb523fb21327bc98c01
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def total(s0, s1, player=None):
          ...     return player, str(s0 + s1)
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=total)
          46caef5ffd6d72c8757279cbcf01b12f
          c42887e7b9ffe8fc26bb57b61329f916
          872dbe4a4fe5d8451aa842c21194c866
          26dad951f8e75106f151e4085e117edd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def echo_0(s0, s1, player=None):
          ...     return player, f"* {s0}" # message of the form: "* s0"
          >>> def echo_1(s0, s1, player=None):
          ...     return player, f"** {s1}" # message of the form: "** s1"
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=5, say=both(echo_0, echo_1))
          3f321d5ce997d2f3989685f56de8bdce
          4a64fe964dc771a219ed773c3a146c75
          3f321d5ce997d2f3989685f56de8bdce
          cad0f4cdee6d8af26abb184d977c50fd
          493e127f779e284556086802640185a8
          cad0f4cdee6d8af26abb184d977c50fd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(3), always_roll(3), dice=make_test_dice(1, 2, 3, 3), goal=8, say=both(say_scores, announce_lead_changes))
          Player 0 now has 1 and now Player 1 has 0
          Player 0 takes the lead by 1
          Player 0 now has 1 and now Player 1 has 2
          Player 1 takes the lead by 1
          Player 0 now has 4 and now Player 1 has 2
          Player 0 takes the lead by 2
          Player 0 now has 4 and now Player 1 has 10
          Player 1 takes the lead by 6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, both, announce_lead_changes, say_scores
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
