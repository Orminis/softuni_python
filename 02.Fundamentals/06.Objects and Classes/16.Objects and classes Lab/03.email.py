class Email:      # Шаблон

    def __init__(self, sender, receiver, content):              # instance attributes
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):                                              # Instance methods
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
email_data = input()

while not email_data == "Stop":                             # Събираме всички имейли в един лист като всеки имейл е лист
    sen, rec, cont = email_data.split()
    current_email = Email(sen, rec, cont)
    emails.append(current_email)
    email_data = input()

indexes_mail_to_sent = [int(index) for index in input().split(", ")]

for index_to_send in indexes_mail_to_sent:                      # определените имейли биват променени изпратени
    email = emails[index_to_send]
    email.send()

for email in emails:                                            # извикваме метода и принтирваме
    print(email.get_info())
