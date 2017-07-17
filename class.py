class Human:
	def __init__(self, *args, **kwargs):
		if len(args) >= 2:
			self.name = args[0]
			self.age = args[1]
		elif len(args) == 1:
			self.name = args[0]
			self.age = 20
		else:
			self.name = "John"
			self.age = 20

	def print(self):
		print("Name: {}, Age: {}.".format(self.name, self.age))

class Student(Human):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.university = "LU"

	def print_grade(self, grade=0):
		print("Your grade is: {:.1f}".format(grade))

human1 = Human("Ahmad", 21)
human2 = Human("Zobaida")
human3 = Human()
student1= Student()

human1.print()
human2.print()
human3.print()
student1.print()
student1.print_grade()
student1.print_grade(100)
