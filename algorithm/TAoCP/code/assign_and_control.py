# Algorithm A (ASSIGN). This algorithm includes the steps implied by ASSIGN within a computational
# program, as described above.
#
# Al. [Wait for n < N.] If n = N, stall the program until n < N. (If n = N, no buffers are ready to
# be assigned; but Algorithm B below, which runs in parallel with this one, will eventually succeed
# in producing a green buffer.)
# A2. [CURRENT ← NEXTG.] Set CURRENT ← NEXTG (thereby assigning the current buffer).
# A3. [Advance NEXTG.] Advance NEXTG to the next clockwise buffer.
# Algorithm R (RELEASE). This algorithm includes the steps implied by RELEASE within a computational
# program, as described above.
# R1. [Increase n.] Increase n by one.
#
# Algorithm B (Buffer control). This algorithm performs the actual initiation of I/O operators in
# the machine; it is to be executed “simultaneously” with the main program, in the sense described
# below.
#
# B1. [Compute.] Let the main program compute for a short period of time; step B2. will be executed
# after a certain time delay, at a time when the I/O device is ready for another operation.
# B2. [n = 0?] If n = 0, go to B1. (Thus, if no buffers are red, no I/O action can be performed.)
# B3. [Initiate I/O.] Initiate transmission between the buffer area designated by NEXTR and the I/O
# device.
# B4. [Compute.] Let the main program run for a period of time; then go to step B5 when the I/O
# operation is completed.
# B5. [Advance NEXTR.] Advance NEXTR to the next clockwise buffer.
# B6. [Decrease n.] Decrease n by one, and go to B2.
