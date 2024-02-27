class Control:
    def __init__(self):
        pass

    def turnOn(self):
        self._tv.turnOn(self._tv)

    def turnOff(self):
        self._tv.turnOff(self._tv)

    def canalUp(self):
        self._tv.canalUp(self._tv)

    def canalDown(self):
        self._tv.canalDown(self._tv)

    def volumenUp(self):
        self._tv.volumenUp(self._tv)

    def volumenDown(self):
        self._tv.volumenDown(self._tv)

    def setCanal(self):
        self._tv.setCanal(self._tv)

    def setVolumen(self):
        self._tv.setVolumen(self._tv)
    
    def enlazar(self, televisor):
        self.tv = televisor
        self.tv.setControl(self)

    def setTv(self, televisor):
        self.enlazar(televisor)

    def getTv(self):
        return self.tv