from .abs_auto import AbsAuto


class FordFusion(AbsAuto):
    def start(self):
        print('Ford fusion start:')

    def stop(self):
        print('Ford fusion stopped.')