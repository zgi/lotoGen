# -*- coding: utf-8 -*-
import random

def main():
    max_val = 99
    min_val = 1
    loto_comb_list = []
    print "Pozdravljen v generatorju Lotto kombinacij.\n"
    try:
        nr_numbers = int(raw_input("Vpiši velikost kombinacije: (%d-%d)" % (min_val, max_val)))
        while nr_numbers > max_val or nr_numbers < min_val:
            print "Vpisal si napačno velikost kombinacije. Poskusi ponovno."
            nr_numbers = int(raw_input("Vpiši velikost kombinacije: (%d-%d)" % (min_val, max_val)))
        for x in range(1, nr_numbers + 1):
            rand_nr = random.randint(1, max_val)
            if rand_nr in loto_comb_list:
                print "\nŠtevilo %d je že v kombinaciji, na %s. mestu. Generiram novo število..." % (rand_nr, loto_comb_list.index(rand_nr)+1)
                rand_nr = random.randint(1, max_val)
            loto_comb_list.append(rand_nr)
            print "Dodajam %d. št: %d" % (x, rand_nr)
        print "Tvoja naslednja srečna loto kombinacija je: %s" % loto_comb_list
    except ValueError:
        print "Prosim vnesi število!"


if __name__ == "__main__":
    main()
