from abc import ABC, abstractmethod


class LoadHandler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request: dict):
        pass


class BaseLoadHandler(LoadHandler):
    _next_handler: LoadHandler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: dict):
        if self._next_handler:
            return self._next_handler.handle(request)

        return True


class HardwareLoadHandler(BaseLoadHandler):
    def handle(self, request: dict):
        stat = request.get("stat")
        if stat is None:
            stat = {}
        cpu = request.get("cpu")
        gpu = request.get("gpu")
        stat["cpu"] = cpu != ""
        stat["gpu"] = gpu != ""
        request["stat"] = stat
        if cpu != "" and gpu != "":
            return super().handle(request=request)
        else:
            return False


class BIOSLoadHandler(BaseLoadHandler):
    def handle(self, request: dict):
        stat = request.get("stat")
        if stat is None:
            stat = {}
        bios = request.get("bios")
        stat["bios"] = bios != ""
        request["stat"] = stat
        if bios != "":
            return super().handle(request=request)
        else:
            return False


class OSLoadHandler(BaseLoadHandler):
    def handle(self, request: dict):
        stat = request.get("stat")
        if stat is None:
            stat = {}
        os = request.get("os")
        stat["os"] = os != ""
        request["stat"] = stat
        if os != "":
            return super().handle(request=request)
        else:
            return False


if __name__ == '__main__':
    hw_handler = HardwareLoadHandler()
    bios_handler = BIOSLoadHandler()
    os_handler = OSLoadHandler()
    hw_handler.set_next(bios_handler).set_next(os_handler)

    request = {
        "cpu": "Intel 12th",
        "gpu": "RTX 3070",
        "bios": "American Megatrends",
        "os": "Windows"
    }
    print(hw_handler.handle(request=request))
    print(request)