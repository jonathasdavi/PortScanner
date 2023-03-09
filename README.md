
## Port Scanner

This script is a simple port scanner that allows the user to scan a range of ports on a target host to check for open ports. It also provides the ability to convert an IP address to a domain name and vice versa.

### Installation

This script requires Python 3 to be installed. Additionally, the `scapy` package needs to be installed for this script to work.

To install the required packages, run the following command:

    pip install scapy

### Usage

To use the port scanner, simply run the `port_scanner.py` script with Python. The script will prompt the user to enter the target host's IP address or domain name, as well as the range of ports to scan.

The script will then scan the specified range of ports on the target host and print out a list of open ports, if any are found. If no open ports are found, it will print a message indicating this.

Additionally, the script will display the duration of the scan in seconds and minutes (if the scan took longer than 60 seconds). It will also convert the IP address or domain name to its opposite type and display the result.

### Functionality

#### `scan_ports`

This function scans a range of ports on a target host to check for open ports.

    def scan_ports(host, start_port, end_port):
        """
        Scans a range of ports on a target host to check for open ports.
    
        Args:
            host (str): The IP address or domain name of the target host.
            start_port (int): The first port to scan.
            end_port (int): The last port to scan.
    
        Returns:
            A list of open ports on the target host and the duration of the scan in seconds.
        """

#### `get_domain`

This function converts an IP address to a domain name.

    def get_domain(ip):
        """
        Converts an IP address to a domain name.
    
        Args:
            ip (str): The IP address to convert.
    
        Returns:
            The domain name associated with the IP address or the original IP address if no domain name is found.
        """

#### `get_ip`

This function converts a domain name to an IP address.

    def get_ip(domain):
        """
        Converts a domain name to an IP address.
    
        Args:
            domain (str): The domain name to convert.
    
        Returns:
            The IP address associated with the domain name or the original domain name if no IP address is found.
        """
#### `detect_os`

This function sends an ICMP echo request to a remote host and analyzes the response to determine the operating system running on the remote host.

    def detect_os(ip_address):
        """
        Sends an ICMP echo request to a remote host and analyzes the response to determine the operating system running on the remote host.
    
        Args:
            ip_address (str): The IP address of the remote host.
    
        Returns:
            The name of the operating system running on the remote host.
        """
## License

This script is licensed under the MIT License. See the LICENSE file for more information.
