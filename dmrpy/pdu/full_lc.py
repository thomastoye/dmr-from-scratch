class FullLC:
    def __init__(self, pf, reserved, flco, fid, data, cs_5bit=None):
        """See ETSI TS 102 361-1 Section 9.1.6

        Parameters:
        pf: Protect Flag (1 bit)
        reserved: Reserved (1 bit)
        flco: Full Link Control Opcode (6 bits)
        fid: Feature Set ID (8 bits)
        data: Full LC data (56 bits)
        crc: Full LC CRC, either Reed-Solomon (12,9) FEC or a 5 bit checksum
        """

        self.pf = pf
        self.reserved = reserved
        self.flco = flco
        self.fid = fid
        self.data = data
        self.cs_5bit = cs_5bit

    def create_from_embedded_signalling_binary(binary, checksum):
        # 77 bits
        return FullLC(
            pf=(binary >> 71) & 0x1,
            reserved=(binary >> 70) & 0x1,
            flco=(binary >> 64) & 0x3F,
            fid=(binary >> 56) & 0xFF,
            data=binary & 0xFFFFFFFFFFFFFF,
            cs_5bit=checksum,
        )

    def create_from_header_or_terminator_burst_binary(binary):
        # 96 bits
        return FullLC()

    def create_from_bptr_transmit_matrix(matrix):
        pass
