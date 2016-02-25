# PRE-ALPHA
Will use rhythmic patterns and scales to write melodys.
The rhythmic patterns will (initially) be provided by me.
The scale will be given as a command line argument.

Example of calling program:
./melody-writer --scale C --mode major


## Representing notes
For now, I'll just use the following convention:

A0 - The lowest A on a piano
B0 - The lowest B on a piano
C0 - The lowest C on a piano
(etc.)
A1 - One octave above the lowest A on a piano
B1 - One octave above the lowest B on a piano
(etc.)

So, the number is the piano octave, the letter is the note.
Enharmonics (sharp, flat, sort of like a "flavor") will be represented as a "#" or "b".
For example, 
Ab1 (octave above lowest A, flattened)
Bb4 (four octaves above lowest Bb)
C#3 ("C Sharp")

There may or may not be configuration options for this.

## Representing rhythm
Backslashes will represent an element of groove or repitition (like a bar).
A period '.' will be an articulation
An underscore will be a duration.
An empty space will be silence.
For now, a bar will be either composed of 6 or 8 of these durations. 

	In 6 time.

	/            /            / (silence)
	/.___.___.___/.___.___.___/ ('quarter' notes)
	/._._._._._._/._._._._._._/ ('eigth' notes)
	/._._        /._._        / ('eigth' notes, followed by silence)

(this has some problems, but it will work for now)


## Bringing it together
At first, the program will just output a visual representation of the melody.
./melody-writer --scale C --mode major
a0 a1 g#0 e0 f#0 g#0 a0





