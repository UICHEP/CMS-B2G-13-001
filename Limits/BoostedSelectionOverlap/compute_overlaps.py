#! /usr/bin/env python

from compute_overlap import *

# Main function
if __name__ == "__main__":

    comparator = Comparator('boosted_allhadronic_data.txt')
    comparator.compare('boosted_lepton_data.txt')
    print 'BAH vs BLJ : data'
    print comparator
    print
    del comparator

    comparator = Comparator('boosted_allhadronic_zp2000w1p.txt')
    comparator.compare('boosted_lepton_zp2000w1p.txt')
    print 'BAH vs BLJ : zp2000w1p'
    print comparator
    print
    del comparator

    comparator = Comparator('boosted_allhadronic_zp2000w10p.txt')
    comparator.compare('boosted_lepton_zp2000w10p.txt')
    print 'BAH vs BLJ : zp2000w10p'
    print comparator
    print
    del comparator

    comparator = Comparator('boosted_allhadronic_ttbar.txt')
    comparator.compare('boosted_lepton_ttbar.txt')
    print 'BAH vs BLJ : ttbar'
    print comparator
    print
    del comparator

