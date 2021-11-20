#  Server part

import json
import sys
import socket


from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, DEFAULT_PORT_RANGE_MIN, DEFAULT_PORT_RANGE_MAX
from common.utils import get_message, send_message


def process_client_message(message):
    '''
    in - DICT from client
    out - DICT from client
    :param message:
    :return:
    '''
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Error! Bad Request'
    }


def main():
    '''
    in - command line
    server.py -p 7777 -a 192.168.4.74
    :return:
    '''

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < DEFAULT_PORT_RANGE_MIN or listen_port > DEFAULT_PORT_RANGE_MAX:
            raise ValueError
    except IndexError:
        print('Error! Add number of port after -\'p\'')
        sys.exit(1)
    except ValueError:
        print(
            f'Error! Invalid port range! Value only {DEFAULT_PORT_RANGE_MIN} to {DEFAULT_PORT_RANGE_MAX}')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        print(
            'Error! Add number of address after \'a\'-')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_cient = get_message(client)
            print(message_from_cient)
            response = process_client_message(message_from_cient)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('JSON error, error in client message')
            client.close()


if __name__ == '__main__':
    main()
