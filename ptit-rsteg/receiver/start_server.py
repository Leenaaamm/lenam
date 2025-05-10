import socket

HOST = "0.0.0.0"
PORT = 12345

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((HOST, PORT))
        sock.listen(1)
        print("[*] Receiver ready, waiting for sender...")
        conn, addr = sock.accept()
        print("[*] Connected by {}".format(addr))
    except Exception as e:
        print("[!] Server error: {}".format(e))
        return

    seen_payloads = set()
    hidden_bits = []

    while True:
        data = conn.recv(1024)
        if not data:
            break
        decoded = data.decode(errors='ignore')
        payload = decoded.strip()

        if payload in seen_payloads:
            bit = payload.split('_')[0]
            hidden_bits.append(bit)
            print("[*] Retransmitted packet detected, bit={}".format(bit))
        else:
            seen_payloads.add(payload)
            print("[!] First-time packet (ignored for hidden bit): {}".format(payload))


    message = ""
    for i in range(0, len(hidden_bits), 8):
        byte = hidden_bits[i:i+8]
        if len(byte) < 8:
            break
        message += chr(int("".join(byte), 2))


    with open("hidden_message.txt", "w") as f:
        f.write(message)

    print("[+] Hidden message extracted: {}".format(message))
    conn.close()

if __name__ == "__main__":
    start_server()

