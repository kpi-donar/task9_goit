CONTACTS = {}


def input_error(handler):
	def wrapper(*args, **kargs):
		try:
			return handler(*args, **kargs)
		except KeyError:
			return 'Enter user name'
		except ValueError:
			return 'Give me name and phone please'
		except IndexError:
			return 'Try again'
		except TypeError:
			return 'Give me name and phone please'
	return wrapper


def hello():
	return  "How can I help you?"


def quit_func():
	return 'Good bye!'


def show():
	return CONTACTS

@input_error
def add(data):
	name, phone = create_data(data)
	CONTACTS[name] = phone
	return "Contact added!"

@input_error
def change(data):
	name, phone = create_data(data)
	if name in CONTACTS:
		CONTACTS[name] = phone
		return 'Contact changed'
	else:
		return "This name is not in CONTACTS"

@input_error
def phone_func(name):
	return CONTACTS[name]


def change_input(user_input):
	new_input = user_input
	data = ''
	for key in COMMANDS:
		if user_input.lower().startswith(key):
			new_input = key
			data = user_input[len(new_input):]
			break
	if data:
		return reaction_func(new_input)(data)
	return reaction_func(new_input)()


def reaction_func(reaction):
	return COMMANDS.get(reaction, break_func)


def break_func():
    return 'Wrong enter.'


def create_data(data):
	new_data = data.split()
	name = new_data[0]
	phone = new_data[1]
	if name.isnumeric():
		raise ValueError()
	if not phone.isnumeric():
		raise ValueError()
	return name, phone

COMMANDS = {'hello': hello, 'add': add, 'change': change, 'phone': phone_func, 'show all': show, 'good bye': quit_func, 'close': quit_func, 'exit': quit_func}

@input_error
def main():
	while True:
		user_input = input('Enter command for bot: ')
		result = change_input(user_input)
		print(result)
		if result == 'Good bye!':
			break


if __name__ == '__main__':
	main()