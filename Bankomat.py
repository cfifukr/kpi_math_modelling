import random


class Bankomat:
    def __init__(self):
        self.balance = random.randint(1000, 10000)
        self.valid_cards = {
            (1, 1234): "Card Type A",
            (2, 5678): "Card Type B"
        }
        self.max_attempts = 3
        self.attempts = 0

    def run(self):
        print("Ласкаво просимо до банкомату!")
        while True:
            card_type = int(input("Введіть тип картки (1 або 2): "))
            card_code = int(input("Введіть код картки: "))
            if not self.authenticate_card(card_type, card_code):
                print("Непідтримуваний тип картки.")
                continue

            self.attempts = 0
            while self.attempts < self.max_attempts:
                pin = int(input("Введіть PIN-код: "))
                if self.check_pin(pin):
                    self.show_menu()
                    break
                else:
                    self.attempts += 1
                    if self.attempts < self.max_attempts:
                        print("Невірний код, спробуйте ще раз.")
                    else:
                        print("Картка заблокована.")
                        return

    def authenticate_card(self, card_type, card_code):
        return (card_type, card_code) in self.valid_cards

    def check_pin(self, pin):
        # Для спрощення, PIN завжди 1111
        return pin == 1111

    def show_menu(self):
        while True:
            print("\nМеню:")
            print("1. Стан рахунку")
            print("2. Зняти гроші")
            print("3. Поповнити баланс")
            print("4. Вихід")
            choice = int(input("Виберіть дію: "))

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                self.withdraw_money()
            elif choice == 3:
                self.top_up_balance()
            elif choice == 4:
                print("Дякуємо за використання банкомату. До побачення!")
                return
            else:
                print("Невірний вибір, спробуйте ще раз.")

    def check_balance(self):
        print(f"Стан рахунку: {self.balance} гривень.")

    def withdraw_money(self):
        amount = int(input("Введіть суму для зняття: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Видано готівки: {amount} гривень.")
        else:
            print("Недостатня кількість грошей на рахунку.")

    def top_up_balance(self):
        amount = int(input("Введіть суму для поповнення балансу: "))
        if amount > 0:
            self.balance += amount
            print(f"Баланс успішно поповнено на {amount} гривень.")
        else:
            print("Сума поповнення повинна бути більше нуля.")


bankomat = Bankomat()
bankomat.run()
