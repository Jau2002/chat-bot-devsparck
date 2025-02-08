from makers.models import Maker

class MakerService:
    @staticmethod
    def find_all():
        return Maker.objects.all()