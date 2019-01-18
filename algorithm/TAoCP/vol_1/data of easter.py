# The following algorithm, due to the Neapolitan astronomer Aloysius Lilius and the German Jesuit
# mathematician Christopher Clavius in the late 16th century, is used by most Western churches to
# determine the date of Easter Sunday for any year after 1582.
#
# Algorithm E (Date of Easter). Let Y be the year for which the date of Easter is desired.
# E1. [Golden number.] Set G ← (Y mod 19) + 1. (G is the so-called “golden number” of the year in
# the 19-year Metonic cycle.)
# E2. [Century.] Set C ← Y/100 + 1. (When Y is not a multiple of 100, C is the century number; for
# example, 1984 is in the twentieth century.)
# E3. [Corrections.] Set X ← 3C/4 − 12, Z ← (8C + 5)/25 − 5. (Here X is the number of years, such as
# 1900, in which leap year was dropped in order to keep in step with the sun; Z is a special
# correction designed to synchronize Easter with the moon’s orbit.)
# E4. [Find Sunday.] Set D ← 5Y/4 − X − 10. (March ((−D) mod 7) will actually be a Sunday.)
# E5. [Epact.] Set E ← (11G + 20 + Z − X) mod 30. If E = 25 and the golden number G is greater than
# 11, or if E = 24, then increase E by 1. (This number E is the epact, which specifies when a full
# moon occurs.)
# E6. [Find full moon.] Set N ← 44 − E. If N < 21 then set N ← N + 30. (Easter is supposedly the
# first Sunday following the first full moon that occurs on or after March 21. Actually
# perturbations in the moon’s orbit do not make this strictly true, but we are concerned here with
# the “calendar moon” rather than the actual moon. The Nth of March is a calendar full moon.)
# E7. [Advance to Sunday.] Set N ← N + 7 − ((D + N) mod 7).
# E8. [Get month.] If N > 31, the date is (N − 31) APRIL; otherwise the date is N MARCH.
#
# Write a subroutine to calculate and print Easter date given the year, assuming that the year is
# less than 100000. The output should have the form “dd MONTH, yyyyy” where dd is the day and yyyyy
# is the year. Write a complete MIX program that uses this subroutine to prepare a table of the
# dates of Easter from 1950 through 2000.
