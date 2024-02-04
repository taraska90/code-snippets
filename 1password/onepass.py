import getpass
import subprocess

def get_auth_data(item_name, auth_flag='1pass'):
    """
    This is a quick example how to handle op cli application
    :param item_name:
    :param auth_flag:
    :return:
    """
    user = ''
    password = ''
    if auth_flag == 'cli':
        user = input("Please enter username:\n")
        password = getpass.getpass(prompt='Enter switch password:\n')
    elif auth_flag == "1pass":
        one_password_output = subprocess.run(["op", "item", "get", item_name, "--fields", "username,password"], stdout=subprocess.PIPE)
        user, password = (((one_password_output.stdout.decode()).rstrip()).split(','))
    else:
        return "no auth flag found"
    authen_data = {'user': user, 'password': password}
    return authen_data


if __name__ == "main":
    print(get_auth_data())