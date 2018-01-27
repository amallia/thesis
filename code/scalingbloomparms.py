#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import math
import matplotlib.pyplot as plt

N0 = 128   # number of 8-byte ints in intlist before we switch to bloom
E = 0.003  # desired false-positive error rate
P = 0.5    # desired fill ratio
R = 0.85   # tightening ratio
S = 2.0    # growth ratio

def log2(x):
    return math.log(x) / math.log(2)

class AsciiOutput:
    FMT = "%2s: %4s %7s | %16s %16s %16s | %16s %16s | %10s %10s"

    def __init__(self):
        print(self.FMT % ("", "Hash", "Checks", "Partition size", "Step size", "Step count", "Tot size", "Tot count", "Flt err", "Tot err"))
        print("-"*130)

    @staticmethod
    def intWithCommas(x):
        if x < 0:
            return '-' + intWithCommas(-x)
        result = ''
        while x >= 1000:
            x, r = divmod(x, 1000)
            result = ",%03d%s" % (r, result)
        return "%d%s" % (x, result)

    def printline(self, *args):
        args = list(args)
        args[3:-2] = [self.intWithCommas(a) for a in args[3:-2]]
        args[-2] = "%.5f" % args[-2]
        args[-1] = "%.5f" % args[-1]
        print(self.FMT % tuple(args))

    def finalize(self):
        pass

class TexOutput:
    def __init__(self):
        print(r"% Generato da scalingbloomparms.py")
        print(r"\begin{tabular}{ r | c c r r | c c r r }")
        print(r"    \hline")
        print(r"    \rowcolor{blue!20}           & \multicolumn{4}{c}{Singolo filtro} & \multicolumn{4}{c}{Totale catena} \\")
        print(r"    \rowcolor{blue!20} n. filtri & $K$ & $E$ & $M$ & $N$              & $K$ & $E$ & $M$ & $N$ \\")
        print(r"    \hline")
        self.row = 0
    def printline(self, *args):
        args = list(args)
        args[0] += 1
        args[:-2] = [r"\num{%d}" % a for a in args[:-2]]
        args[-1] = r"\SI{%.3f}{\%%}" % (args[-1]*100)
        args[-2] = r"\SI{%.3f}{\%%}" % (args[-2]*100)
        idx, k, ck, s, m, n, cm, cn, e, ce = args
        self.row += 1
        if self.row % 2 == 1:
            print(r"    \rowcolor[gray]{0.925}")
        print(r"    " + " & ".join([idx, k, e, m, n, ck, ce, cm, cn]) + r" \\")
    def finalize(self):
        print(r"    \hline")
        print(r"\end{tabular}%")

out = TexOutput()

# Compute first N so that first M (memory size) is about double the size
# of the first intlist. Doubling memory size as we grow is an acceptable
# pattern.
E0 = E * (1-R)
N0 = int(S * N0 * 64 * ((math.log(P) * math.log(1.0-P)) / abs(math.log(E0))))

TNS = []
ES = []
TES = []
KS = []
TKS = []
MS = []
TMS = []

efinal = 1
cnt = 0
tot = 0
hfn = 0
for i in range(24):
    e = E0 * math.pow(R, i)
    n = N0 * math.pow(S, i)
    efinal *= 1-e

    k = int(math.ceil(-log2(e)))
    m = n / ((math.log(P) * math.log(1.0-P)) / abs(math.log(e)))
    m = int((m+7)/8)
    m = (m + 63) / 64 * 64
    tot += m
    cnt += n
    hfn += k

    out.printline(i, k, hfn, int(m/k), m, n, tot, cnt, e, 1-efinal)

    KS.append(k)
    ES.append(e)
    MS.append(m)
    TNS.append(cnt)
    TES.append(1-efinal)
    TKS.append(hfn)
    TMS.append(tot)

out.finalize()

if False:
    # Error graph ------------------------------------

    plt.plot(TNS, ES, "b-", label="Singolo filtro")
    plt.plot(TNS, TES, "r-", label="Totale")
    plt.plot(TNS, [E]*len(TNS), "r--")
    plt.legend()

    plt.ylabel("probabilità falso positivo")
    plt.xlabel("numero di elementi")
    plt.xscale("log")

    plt.tight_layout()
    plt.savefig("scalingbloom_error.pdf")
    plt.show()
    plt.close()

    # Hash graph -------------------------------------

    plt.plot(TNS, KS, "b-", label="Singolo filtro")
    plt.plot(TNS, TKS, "r-", label="Totale")
    plt.legend()

    plt.ylabel("numero funzioni di hash")
    plt.xlabel("numero di elementi")
    plt.xscale("log")

    plt.tight_layout()
    plt.savefig("scalingbloom_hash.pdf")
    plt.show()
    plt.close()

    # Memory graph -----------------------------------

    plt.plot(TNS, MS, "b-", label="Singolo filtro")
    plt.plot(TNS, TMS, "r-", label="Totale")
    plt.legend()

    plt.ylabel("memoria utilizzata")
    plt.xlabel("numero di elementi")

    plt.tight_layout()
    plt.savefig("scalingbloom_memory.pdf")
    plt.show()
    plt.close()
