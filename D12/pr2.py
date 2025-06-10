
class Headmaster:
    def lead(self):
        print("\nHeadmaster leads the school.")

class Teacher(Headmaster):
    def teach(self):
        print("Teacher teaches students.")

class Administrator(Headmaster):
    def manage(self):
        print("Administrator manages school activities.")


chalk = Teacher()
form = Administrator()

chalk.lead()
chalk.teach()

form.lead()
form.manage()


