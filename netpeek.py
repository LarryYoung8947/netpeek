import socket
import subprocess

def get_local_ip():
	hostname = socket.gethostname()
	ip_addy = socket.gethostbyname(hostname)
	return ip_addy

ip_address = get_local_ip()

def get_network_prefix(address): 
	parts = address.split(".")
	prefix = f"{parts[0]}.{parts[1]}.{parts[2]}"
	return prefix

prefix = get_network_prefix(ip_address)

def generate_ip_addresses(prefix):
	addresses = []
	for number in range(1, 255):
		address = f"{prefix}.{number}"
		addresses.append(address)
	return addresses

addresses = generate_ip_addresses(prefix)

def ping_device(address):
	result = subprocess.run(
		["ping", "-n", "1", address],
		capture_output=True
	)
	return result.returncode == 0

def scan_network(addresses):
	online_devices = []
	for address in addresses:
		print(f"Scanning {address}...")
		if ping_device(address):
			online_devices.append(address)
	return online_devices
		

online_devices = scan_network(addresses)
print(online_devices)



