import requests


class ECODEVICE:
    """Class representing the ECODEVICE RT2 and its API"""

    def __init__(self, host, port=80, apikey=""):
        self._host = host
        self._port = port
        self._apikey = apikey
        self._api_url = f"http://{host}:{port}/api/xdevices.json?key={apikey}"

    @property
    def host(self):
        return self._host

    @property
    def apikey(self):
        return self._apikey

    def _request(self, params):
        r = requests.get(self._api_url, params=params, timeout=2)
        r.raise_for_status()
        content = r.json()
        product = content.get("product", None)
        if product == "EcoDevices_RT":
            return content
        else:
            raise Exception(
                "Eco-Devices api request error, url: %s`r%s", r.request.url, content,
            )

    def ping(self) -> bool:
        try:
            self._request({"Index": "All"})
            return True
        except:
            pass
        return False

    def get(self, rt2_in, rt2_in_detail, rt2_name) -> int:
        """Get value from api : http://{host}:{port}/api/xdevices.json?key={apikey}&{rt2_in}={rt2_in_detail}, then get value {rt2_name} in JSON response"""

        return self._request({rt2_in: rt2_in_detail}).get(rt2_name)
