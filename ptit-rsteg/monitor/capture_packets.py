import subprocess

def capture():
    cmd = ["tcpdump", "-i", "any", "-w", "captured_retrans.pcap"]
    print("[*] Capturing packets with tcpdump...")
    try:
        subprocess.call(cmd)
    except Exception as e:
        print("[!] Failed to run tcpdump: {}".format(e))

if __name__ == "__main__":
    capture()
