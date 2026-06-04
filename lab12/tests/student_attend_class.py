test = {
  'name': 'student_attend_class',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define student-john (student-create 'john '(astronomy))) ; a student named John who has attended astronomy once
          student-john
          scm> (define student-john (student-attend-class student-john 'chemistry))
          student-john
          scm> (student-get-classes student-john)
          (chemistry astronomy)
          scm> (define student-john (student-attend-class student-john 'history))
          student-john
          scm> (student-get-classes student-john)
          (history chemistry astronomy)
          scm> (student-get-name student-john)
          john
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
          scm> (define student-john (student-create 'john '(astronomy))) ; a student named John who has attended astronomy once
          student-john
          scm> (define student-john (student-attend-class student-john 'chemistry))
          student-john
          scm> (student-get-classes student-john)
          (chemistry astronomy)
          scm> (define student-john (student-attend-class student-john 'history))
          student-john
          scm> (student-get-classes student-john)
          (history chemistry astronomy)
          scm> (student-get-name student-john)
          john
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load "./lab12.scm")
      scm> (load "./tests/alternate_teachers_students.scm")  ; abstraction check: load different abstraction!
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
