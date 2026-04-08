import re  # for pattern matching


def identify_server(banner):

    # If no banner → nothing to detect
    if banner is None:
        return ("Unknown", "Unknown", "Unknown")

    server = "Unknown"
    version = "Unknown"
    os = "Unknown"

    # Split banner into lines
    lines = banner.split("\n")

    # Look for "Server:" header
    for line in lines:
        if line.lower().startswith("server:"):
            server_info = line.split(":", 1)[1].strip()
            server = server_info

            # Try extracting version (like Apache/2.4.41)
            version_match = re.search(r"/([0-9\.]+)", server_info)
            if version_match:
                version = version_match.group(1)

            break

    banner_lower = banner.lower()  # (not used much, but kept)

    # Try extracting OS info inside brackets (like (Ubuntu))
    os_match = re.search(r"\((.*?)\)", banner)
    if os_match:
        os = os_match.group(1)

    return server, version, os