class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment

#Тесты
# создать экземпляр, не имея значения hours   
employee1 = EmployeeSalary.get_hours('Sveta', 2, 'sveta@mail.ru')
print(f'Для первого сотрудника установлено часов рабочего времени: {employee1.hours}') #40

#Рассчет ЗП
print(f'Зароботная плата первого сотрудника: {employee1.salary()}')

#создать экземпляр, не имея email
employee2 = EmployeeSalary.get_email('Maria', 48, 1)
print(f'Для второго сотрудника установлена почта: {employee2.email}') #Maria@email.com

# разные значения hourly_payment
print(f'Ставка сотрудника до изменения: {employee2.hourly_payment}') #400 - экземпляр до замены ставки
EmployeeSalary.set_hourly_payment(100)
print(f'Ставка сотрудника после изменения: {employee2.hourly_payment}') #100 - экземпляр после замены ставки
