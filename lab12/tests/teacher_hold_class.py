test = {
  'name': 'teacher_hold_class',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define student-john (student-create 'john '(astronomy)))
          student-john
          scm> (define student-jamie (student-create 'jamie '(astronomy astronomy)))
          student-jamie
          scm> (define students (cons student-john (cons student-jamie nil)))
          students
          scm> (define teacher-pamela (teacher-create 'pamela 'cs61a students))
          teacher-pamela
          scm> (define teacher-pamela (teacher-hold-class teacher-pamela)) ; pamela holds class!
          teacher-pamela
          scm> (map student-get-name (teacher-get-students teacher-pamela))
          (john jamie)
          scm> (map student-get-classes (teacher-get-students teacher-pamela))
          ((cs61a astronomy) (cs61a astronomy astronomy))
          scm> (define teacher-paul (teacher-create 'paul 'cs61b (teacher-get-students teacher-pamela))) ; paul works with pamela's students
          teacher-paul
          scm> (define teacher-paul (teacher-hold-class teacher-paul)) ; paul holds class!
          teacher-paul
          scm> (map student-get-classes (teacher-get-students teacher-paul))
          ((cs61b cs61a astronomy) (cs61b cs61a astronomy astronomy))
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
          scm> (define student-john (student-create 'john '(astronomy)))
          student-john
          scm> (define student-jamie (student-create 'jamie '(astronomy astronomy)))
          student-jamie
          scm> (define students (cons student-john (cons student-jamie nil)))
          students
          scm> (define teacher-pamela (teacher-create 'pamela 'cs61a students))
          teacher-pamela
          scm> (define teacher-pamela (teacher-hold-class teacher-pamela)) ; pamela holds class!
          teacher-pamela
          scm> (map student-get-name (teacher-get-students teacher-pamela))
          (john jamie)
          scm> (map student-get-classes (teacher-get-students teacher-pamela))
          ((cs61a astronomy) (cs61a astronomy astronomy))
          scm> (define teacher-paul (teacher-create 'paul 'cs61b (teacher-get-students teacher-pamela))) ; paul works with pamela's students
          teacher-paul
          scm> (define teacher-paul (teacher-hold-class teacher-paul)) ; paul holds class!
          teacher-paul
          scm> (map student-get-classes (teacher-get-students teacher-paul))
          ((cs61b cs61a astronomy) (cs61b cs61a astronomy astronomy))
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
