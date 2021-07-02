# ETSI TS 102 361-1 Section 9.1.2


class Emb:
    def __init__(self, cc, pi, lcss, fec=None):
        """
        Parameters:
        cc: Colour code (4 bits)
        pi: Pre-emption and power control indicator (1 bit)
        lcss: Link Control Start/Stop (2 bits)
        fec: Parity bits (9 bits), Quadratic Residue (16,7,6)
        """

        self.cc = cc
        self.pi = pi
        self.lcss = lcss

        # TODO if fec is none, calculate parity
        self.fec = fec

    def __repr__(self):
        return f"Emb(cc={hex(self.cc)}, pi={hex(self.pi)}, lcss={hex(self.lcss)}, fec={hex(self.fec)})"

    def raw(self):
        return (self.cc << 12) + (self.pi << 11) + (self.lcss << 9) + self.fec

    def has_valid_fec(self):
        # TODO Quadratic Residue (16,7,6)
        pass

    def create_from_binary(data):
        # Data is 16 bits

        return Emb(
            cc=(data >> 12) & 0xF,
            pi=(data >> 11) & 0x1,
            lcss=(data >> 9) & 0x3,
            fec=data & 0x1FF,
        )
