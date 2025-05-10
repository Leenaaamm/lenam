import socket
import time
import json

MESSAGE = "SECRET123"
SERVER_IP = "172.10.0.4"
SERVER_PORT = 12345

def text_to_bitstream(text):
    bitstream = ''.join(format(ord(c), '08b') for c in text)
    return list(bitstream)

def send_message_with_retrans():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((SERVER_IP, SERVER_PORT))
        print("[*] Connected to receiver.")
    except Exception as e:
        print("[!] Connection failed: {}".format(e))
        return

    bits = text_to_bitstream(MESSAGE)

    for i, bit in enumerate(bits):
        payload = "{}_{}".format(bit, i)
        try:
            sock.send(payload.encode())
            print("[*] Sent bit {} as payload: {}".format(bit, payload))
            time.sleep(0.5)
            sock.send(payload.encode())
            print("[*] Re-sent bit {} as payload: {}".format(bit, payload))
        except Exception as e:
            print("[!] Send failed at bit {}: {}".format(i, e))
        time.sleep(0.5)
    with open("result_signal_bits.txt", "w") as f:
        f.write(json.dumps(bits))

    sock.close()

if __name__ == "__main__":
    send_message_with_retrans()

