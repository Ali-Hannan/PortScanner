from socket import *
import random

# Fun facts list (global scope)
fun_facts = [
    "A group of flamingos is called a flamboyance.",
    "The average person spends six months of their lifetime waiting for red lights to turn green.",
    "Giraffes have the same number of neck vertebrae as humans: seven.",
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    "The total weight of all the ants on Earth is greater than the weight of all the humans.",
    "The Hawaiian alphabet only has 13 letters.",
    "The shortest war in history was between Britain and Zanzibar in 1896. Zanzibar surrendered after 38 minutes.",
    "Cows have best friends and can become stressed when they are separated.",
    "In Switzerland, it is illegal to own just one guinea pig because they are social animals.",
    "A single strand of spaghetti is called a 'spaghetto'.",
    "The human brain generates enough electricity to power a small LED light."
]

def getPortKeyword(port):
    port_keywords = {
        21: 'FTP',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        53: 'DNS',
        80: 'HTTP',
        110: 'POP3',
        143: 'IMAP',
        443: 'HTTPS',
        3389: 'RDP'
    }
    return port_keywords.get(port, 'Unknown')

def conScan(tgtHost, tgtPort):
    result = {}
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.settimeout(1)
        connskt.connect((tgtHost, tgtPort))
        result["port"] = tgtPort
        result["status"] = "open"
        result["service"] = getPortKeyword(tgtPort)
        result["fun_fact"] = random.choice(fun_facts)
        connskt.close()
    except:
        result["port"] = tgtPort
        result["status"] = "closed"
        result["service"] = getPortKeyword(tgtPort)
    return result

# ✅ Refactored to support Flask API input
def portScan(tgtHost, tgtPorts):
    results = []
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        return [{"error": f"Cannot resolve host: {tgtHost}"}]

    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print(f"Scanning port: {tgtPort}")
        scan_result = conScan(tgtIP, tgtPort)
        results.append(scan_result)

    return results
