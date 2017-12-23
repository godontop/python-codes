// update by YWH 2017.12.23
function FindProxyForURL(url, host) {
    var xtunnel = 'SOCKS 192.168.1.175:1080';
    if (dnsDomainIs(host, 'google.com') ||
        dnsDomainIs(host, 'www.google.com'))
        return xtunnel;

// DEFAULT RULE: All other traffic
    return "DIRECT";
}
