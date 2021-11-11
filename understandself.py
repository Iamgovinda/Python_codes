class student:

    def info(self):
        return f"Name: {self.name}\nAge: {self.age}\nRoll_no: {self.roll_no}"

Ram = student()
Hari = student()

Ram.name="Ram"
Ram.age=21
Ram.roll_no=3

Hari.name="Hari"
Hari.age=23
Hari.roll_no=5

print(Ram.info())