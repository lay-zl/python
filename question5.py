class Subject(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Student(models.Model):
   name = models.CharField(max_length=128)
   reg_no = models.CharField(max_length=16, unique=True)
   modified = models.DateTimeField(auto_now=True)


class StudentMarks(models.Model):
   student = models.ForeignKey(Student)
   subject = models.ForeignKey(Subject)
   score = models.IntegerField()
   exam_date = models.DateField()



"""
>>> get_total_score(exam_date_year=2019)
  { 'REGNO001': 625.00, 'REGNO002': 325.00, ..... }
"""

# Assuming data already exists in the System.
# Complete code using Django ORM to find total marks across all subjects in a given year.
def get_total_score(exam_date_year):  # Returns reg_no : total_marks
   pass


"""
>>> get_subjectwise_ranks(exam_date_year=2019)
  {
    'Physics': ['REGNO005','REGNO004','REGNO003'... ],
    'Chemistry': ['REGNO004','REGNO005','REGNO003'... ],
    ..
}

"""
# Assuming data already exists in the System. 
# Complete code using Django ORM to find reg no of students Subject wise ranking 
def get_subjectwise_ranks(exam_date_year, subject_name):
   pass


"""
>>> get_highest_scorer_details_for_subject(exam_date_year=2019, subject_name='Physics')
  [ {'name':'Ramesh','reg_no':'REGNO005'}, ... ]

"""
# Assuming data already exists in the System. 
# Complete code using Django ORM to find details of highest scorer in a given subject for a given year.
def get_highest_scorer_details_for_subject(exam_date_year, subject_name):
   pass
