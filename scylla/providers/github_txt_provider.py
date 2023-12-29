from scylla.providers.plain_text_provider import PlainTextProvider

class TheSpeedXProvider(PlainTextProvider):

    def urls(self) -> [str]:
        return [
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt',
            'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt',
            'https://sunny9577.github.io/proxy-scraper/proxies.txt',
            'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt',
            'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
            'https://github.com/prxchk/proxy-list/blob/main/socks4.txt',
            'https://github.com/prxchk/proxy-list/blob/main/socks5.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt',
            'https://github.com/ErcinDedeoglu/proxies/blob/main/proxies/https.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt',
            'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt',
        ]
