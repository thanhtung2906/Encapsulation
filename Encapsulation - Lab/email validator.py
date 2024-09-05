class EmailValidator:
    def __init__(self,min_length,mails,domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains
    def validate_name(self,name):
        if len(name) <= self.min_length:
            return True
        else:
            return False
        
    def validate_mail(self,mail):
        if mail in self.mails:
            return True
        else: 
            return False
    def validate_domain(self,domain):
        if domain in self.domains:
            return True
        else:
            return False
    def validate(self,email:str):
        name = email.split("@")
        a = email.split('@')
        mail = a[1].split('.')
        domain =  email.split(".")
        
        if self.validate_name(name[0]) and self.validate_mail(mail[0]) and self.validate_domain(domain[1]):
            return True
        else:
            return False 


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
             
    