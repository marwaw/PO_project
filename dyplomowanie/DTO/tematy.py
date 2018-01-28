class TematDTO(object):

    def __init__(self, id, tresc_pl, promotor, status = None):
        self.id = id
        self.tresc_pl = tresc_pl
        self.promotor = promotor
        self.status = status

    def __eq__(self, other):
        return (self.id == other.id
                and self.tresc_pl == other.tresc_pl
                and self.promotor == other.promotor
                and self.status == other.status)