class TematDTO(object):

    def __init__(self, id, tresc_pl, promotor, status = None):
        self.id = id
        self.tresc_pl = tresc_pl
        self.promotor = promotor
        self.status = status