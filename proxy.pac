// update by YWH 2017.12.23
function FindProxyForURL(url, host) {
    var xtunnel = 'SOCKS 192.168.1.175:1080';
    if (shExpMatch(host, '*.google.com') ||
        shExpMatch(host, '*.amazonaws.com'))
        return xtunnel;

// DEFAULT RULE: All other traffic
    return "DIRECT";
}
