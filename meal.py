from datetime import datetime

class FoodDiary:

    def __init__(self):
        self._json = {}

    def add_meal(self, meal):
        date = self._get_date()
        if date in self._json:
            self._json[date].append(meal)
        else:
            self._json[date] = [meal]
        return "OK, it's done"

    def list_meal(self, date):
        if date in self._json:
            return "\n".join(self._json[date])
        return "No meals for that day"

    def _get_date(self):
        today = datetime.now()
        return "{}.{}.{}".format(today.day, today.month, today.year)



class CLI:

    def __init__(self, diary):
        self.commands = {
            "meal": diary.add_meal,
            "list": diary.list_meal
            }
        
    def _create_hello_message(self):
        return "hello"

    def _create_menu_message(self):
        return "help text"

    def start(self):
        print(self._create_hello_message())
        print(self._create_menu_message())

        while True:
            console_input = input("Enter command: =>")
            try:
                text = console_input.split()
                command = text[0]
                if command =="exit":
                    break
                parameter = text[1]
            except:
                print("command as first argument and second parameter are expected")
            print(self.commands[command](parameter))

def main():
    diary = FoodDiary()
    interface= CLI(diary)
    interface.start()

if __name__ == "__main__":
    main()
