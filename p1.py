# wapp to detect grade of student using OOP

class student:
	def __init__(self, rno, name, marks):
		self.rno = rno
		self.name = name
		self.marks = marks
	def show(self):
		print("rno = ", self.rno)
		print("name = ", self.name)
		print("marks = ", self.marks)
	def find_grade(self):
		if self.marks > 80:
			print("Grade A ")
		elif self.marks > 60:
			print(" Grade B")
		else:
			print(" Grade C")
rno = int(input(" enter your rno "))
name = input(" enter your name ")
marks = int(input(" enter your marks "))

s = student(rno, name, marks)
s.show()
s.find_grade()


	