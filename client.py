# Client

import socket
import json
import time
import sys


from common.variables import ACTION, ACCOUNT_NAME, PRESENCE, TIME, USER,  \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, DEFAULT_PORT_RANGE_MIN, DEFAULT_PORT_RANGE_MAX,  \
    RESPONSE_200, RESPONSE_400
from common.utils import send_message, get_message


def create_presence(account_name='Guest'):
    '''
    :param account_name:
    :return:
    '''

    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):
    '''
    :param message:
    :return:
    '''
    if RESPONSE in message:
        if message[RESPONSE] == RESPONSE_200:
            return f'{RESPONSE_200} : OK'
        return f'{RESPONSE_400} : {message[ERROR]}'
    raise ValueError


def main():
    '''
    info from command line
    '''

    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < DEFAULT_PORT_RANGE_MIN or server_port > DEFAULT_PORT_RANGE_MAX:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print( f'Error! Invalid port range! Value only {DEFAULT_PORT_RANGE_MIN} to {DEFAULT_PORT_RANGE_MAX}')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Error! Decode error')


if __name__ == '__main__':
    main()
