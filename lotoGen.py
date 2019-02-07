# -*- coding: utf-8 -*-
import random

def main():
    loto_comb_list = []
    print "Pozdravljen v generatorju Lotto kombinacij.\n"
    try:
        nr_numbers = int(raw_input("Vpiši velikost kombinacije: (1-99)"))
        while nr_numbers > 99 or nr_numbers < 1:
            print "Vpisal si napačno velikost kombinacije. Poskusi ponovno."
            nr_numbers = int(raw_input("Vpiši velikost kombinacije: (1-99)"))
        for x in range(1, nr_numbers + 1):
            rand_nr = random.randint(1, 100)
            if rand_nr in loto_comb_list:
                print "\nŠtevilo %d je že v kombinaciji, na %s. mestu. Generiram novo število..." % (rand_nr, loto_comb_list.index(rand_nr)+1)
                rand_nr = random.randint(1, 100)
            loto_comb_list.append(rand_nr)
            print "Dodajam %d. št: %d" % (x, rand_nr)
        print "Tvoja naslednja srečna loto kombinacija je: %s" % loto_comb_list
    except ValueError:
        print "Prosim vnesi število!"


if __name__ == "__main__":
    main()