# Digital Mobile Radio (DMR) from scratch

This project is my attempt to decode [Digital Mobile Radio](https://en.wikipedia.org/wiki/Digital_mobile_radio) (DMR) from scratch in idiomatic, modern Python. It's optimized for legibility and ease of understanding rather than performance.

## Development

```
$ nix-shell
$ make test
```

## Resources and references

ETSI standard (*ETSI TS 102 361*):

1. [Air interface protocol](https://www.dmrassociation.org/downloads/standards/ts_10236101v020501p.pdf)
2. [DMR voice and generic services](https://www.dmrassociation.org/downloads/standards/ts_10236102v020401p.pdf)
3. [Data protocol](https://www.dmrassociation.org/downloads/standards/ts_10236103v010301p.pdf)
4. [Trunking protocol](https://www.dmrassociation.org/downloads/standards/ts_10236104v011001p.pdf)


Other projects:

* [DMRDecode](https://github.com/IanWraith/DMRDecode)
* [mbelib](https://github.com/szechyjs/mbelib)
* [dsd](https://github.com/szechyjs/dsd)
* [go-dmr](https://github.com/pd0mz/go-dmr)
* [dmr_utils3](https://github.com/HBLink-org/dmr_utils3)


Assets and example files:

* [SDRSharp_20160101_231914Z_12kHz_IQ.wav](https://www.sigidwiki.com/wiki/File:DMR.zip), [source](https://www.sigidwiki.com/wiki/Digital_Mobile_Radio_(DMR))

## Implementation of error-correcting codes and checksums

DMR uses a lot of different error-correcting codes and checksums. The description of the FEC and CRC codes used can be found in ETSI TS 102 361-1 Annex B.

* Block Product Turbo Codes (BPTC)
    * BPTC(196,96)
    * Variable length BPTCs
* Rate 3/4 Trellis Code
* Quadratic Residue (16,7,6)
* Golay (20,8,7)
* Hamming Codes
  * Hamming (7,4,3)
  * Hamming (13,9,3), Hamming (15,11,3), Hamming (16,11,4): Used in BPTC
* Reed-Solomon (12,9,4)
* 8-bit CRC, 32-bit CRC, CRC-CCITT, CRC-9, 7-bit CRC, CRC mask for Data Types
* 5-bit Checksum

## Currently working on

* Decoding full LCs from voice superframes
