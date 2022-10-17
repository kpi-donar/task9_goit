CONTACTS = {}

def input_error(handler):
	def wrapper(*args, **kargs):
		try:
			res = handler(*args, **kargs)
			return res
		except KeyError:
			print('Enter user name')
		except ValueError:
			print('Give me name and phone please')
		except IndexError:
			print('Try again')
		except TypeError:
			print('Give me name and phone please')
	return wrapper


def hello():
	return  "How can I help you?"


def quit_func():
	print('Good bye!')
	quit()


def show():
	return CONTACTS

@input_error
def add(name, phone):
	CONTACTS[name] = phone
	return "Contact added!"

@input_error
def change(name, phone):
	if name in CONTACTS:
		CONTACTS[name] = phone
		return 'Contact changed'
	else:
		return "This name is not in CONTACTS"

@input_error
def phone_func(name):
	return CONTACTS[name]

@input_error
def main():
	COMMANDS = {'hello': hello, 'add': add, 'change': change, 'phone': phone_func, 'show_all': show, 'good bye': quit_func, 'close': quit_func, 'exit': quit_func}

	while True:
		command = input("Input command:").lower()
		command = command.split()
		if len(command) == 1 and command[0] in COMMANDS:
			print(COMMANDS[command[0]]())
		elif len(command) == 2 and command[0] in COMMANDS:
			print(COMMANDS[command[0]](name = command[1]))
		elif len(command) == 3 and command[0] in COMMANDS:
			print(COMMANDS[command[0]](name = command[1], phone = command[2]))


if __name__ == '__main__':
	main()