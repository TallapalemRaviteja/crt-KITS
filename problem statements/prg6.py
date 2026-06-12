class Client:
    def __init__(self, name):
        self.name = name


class Project:
    def __init__(self, project_name, hours, rate):
        self.project_name = project_name
        self.hours = hours
        self.rate = rate

    def invoice_amount(self):
        return self.hours * self.rate


class Invoice:
    def __init__(self, client, project):
        self.client = client
        self.project = project

    def generate_invoice(self):
        print("=" * 50)
        print("                CLIENT INVOICE")
        print("=" * 50)
        print(f"\nClient Name    : {self.client.name}")
        print(f"Project Name   : {self.project.project_name}")
        print(f"Hours Worked   : {self.project.hours}")
        print(f"Hourly Rate    : ₹{self.project.rate}")
        print(f"\nInvoice Amount : ₹{self.project.invoice_amount()}")
        print("\n" + "=" * 50)


client_name = input("Client Name: ")
project_name = input("Project Name: ")
hours = int(input("Hours Worked: "))
rate = int(input("Hourly Rate: "))

client = Client(client_name)
project = Project(project_name, hours, rate)

invoice = Invoice(client, project)
invoice.generate_invoice()