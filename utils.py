def int_input(message, min=None, max=None):
    while True:
        try:
            value = int(input(message + ': '))
            
            if (min is not None and value < min) or (max is not None and value > max):
                print(f"Enter a number between {min} and {max}.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")
            
def prompt_yn(message):
    while True:
        value = input(message + ' (y/n): ').lower()
        
        if value in ['y', 'yes']:
            return True
        elif value in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")

def install_app(app_name):
    print(f"Installing {app_name}...")
    
    # TODO: Install via chocolatey