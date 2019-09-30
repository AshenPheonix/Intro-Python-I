"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt') as f:
    print(f.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt','w') as f:
    f.write("""Dylan sat in the silver chair, leaning slightly back and crossing his legs. His short, brown hair was slicked back tight to his head, almost like a helmet in appearance and shine. His steel gray eyes were fixed on the amber brown liquid, \"whiskey\" he had called it, swirling slowly in the glass tumbler in his hands. The pair of large ice cubes made a clicking noise as they circumnavigated the glass slowly. The liquid, a poison according to the sensors, had given the man's lips a light pink color. His jacket and pants, both made of a loose Plasticine type of material, shone dark blue in the light of the conference table.
        
Human, they had called themselves, and this was their commander. Not of their entire military, but of this one vessel. This was, hopefully, the beginning of peaceful contact with the race. He wasn't the only being at the table, but he was the one everyone else was focused on.

Dylan glanced his eyes around, looking at each of the other beings in turn, each scan short but precise. Several furred creatures, each of the 6 a different race but apparently from the same planet, sat to his left. They had called themselves something unpronounceable to Dylan, but insisted on the name \"Felis\" for those outside their race. It was a common theme, apparently. Done in an attempt to allow others to communicate even without the full benefit of identical vocal boxes. Each of the Felis had different colored fur, and each a different ear style, some closer to cats and others closer to dogs. One even could have been bunny ears. They all had tails as well, prehensile from what Dylan could see, though he wasn't yet convinced they were fully under the control of the accompanying creature. They wore what would be best described as bikinis, bits of fabric that seemed almost as much for fashion as anything else. Many of them had bangles knotted in their fur.

Opposite Dylan, a thick skinned race called Focal that reminded Dylan of elephants in the old journals, an extra appendage jutting from where it's nose would be on a human. This being also had a third leg coming out of it's back, and its chair was thus lacking a backing. It's skin was a pale gray color, and it wore leather clothes that looked uncomfortably tight. A scar over it's left eye told of battles long ago fought, the skin underneath a pale pink color.

Beside him, a pair of beings made of rock, Dargan, or some other similar material. Red in color, they gave off a faint glow that seemed to pulse in time with the emotions Dylan would have expected from another being. They spoke through a moving section of stone in the middle of it's crag-like features. Dylan wanted ever so much to feel the texture of the stone, wondering if it would remind him of the mountains back home.

Further on, a pair of thin skinned creatures, Cilone, that lived in a self contained environmental suit. The suits were filled with what looked like water or brine. From this distance, you could only barely make out their pale blue skin as it moved in time with the currents in the suit, generated from a small device Dylan presumed was a filter of some sort. Instead, what you saw was the thick mass of muscle that Dylan presumed was their nervous system, but he wasn't quite sure. He noted a thin ring of lights coming from the inside of their helmets, though could not figure out why.

Beside them, a creature called a Triff, floating in the air with a set of four tentacles, each moving only in the faint air currents in the air. It's skin was a pale pink color, like fresh scar tissue or lightly burned flesh. You could see the pulsing of the veins in the creature's skin, slow and purple blood flowing through the impossibly tough sinews. Dylan couldn't make out anything resembling eyes, but a pair of darkened spots on the dome that made it's central mass always \"looked\" at him when the creature spoke, a thick flap of flesh opening at the bottom of the dome.

\"So,\" Dylan spoke, his head raising finally from the glass, \"Are we all agreed then? We meet again in 2 galactic months to discuss trade agreements and you guys won't attack us at the first sign of us existing?\"

The translator spoke his words in each of the other beings languages as Dylan drank another sip from the glass, the ice cubes finally stopping their constant rapture.

\"Yes,\" One of the Felis spoke, \"Though we are sorry for the loss of your earlier craft, we saw its weapons and presumed it an attack vessel. We are truly sorry for destroying it.\"

Dylan looked up squarely at that being, \"Perfectly understandable. However, we'd appreciate it if you didn't do that next time.\"

The room was silent for a moment, Dylan slowly sliding his eyes over each of the delegates again. As he did so, he noted one of the Cilone head lights had turned off, and it's \"eyes\" had slowly begun to widen. Dylan ignored it, and leaned forwards to speak.

\"Is there an....\" Dylan started. He was rudely interrupted by the Cilone screaming. These were not properly translated, but the Cilone began to skitter backwards, sliding and slipping before tripping and falling down. The rest of the delegates followed Dylan in watching the antics of the being. The second Cilone ran to it's side as it began to hyperventilate, throwing a few levers on the \"filter\" of the creature's suit. The Cilone began to calm down, whimpering quietly as it did so, one word repeated through it's lips. It took a moment for the translator to do it's work, but what came out gave no clarity. It was one word repeated. \"How.\"

\"What's going on?\" Dylan spoke out. Everyone else shook their collective heads, or at least that's the impression that Dylan got. No one answered.

Finally, the second Cilone turned to Dylan before speaking. \"How?\"

Everyone turned to Dylan. He, in turn, shrugged. \"How, what?\"

Dylan noted something in the fluids around the Cilone's head. A kind of blue coloring that seemed to come from it's face.

\"How?\" it repeated.

Dylan looked at the Focal. It brought it's gaze to Dylan, but \"shrugged\" as well.

\"The Cilone are mind readers. Any mated pair are in almost constant contact with one another, only blocked by certain electromagnetic spectrum of light.\" One of the Felis spoke, \"She must be feeling what her mate is.\"

\"Ahh.\" Dylan spoke, sitting back down. He wasn't sure when he had stood up, but he had been.

He grabbed his glass and began swirling it around again, before stopping and downing the remainder of the glass, an amount that surprised the other attendants that had watched him down less than a quarter of what he had just downed over the last few hours.

\"We name our vessels after ancient people and gods.\" Dylan finally said, \"My vessel, the UEG Sherman was named after a general long ago, known for... that's irrelevant, really. It's an attack ship, if need be, and armed as such. The UEG Dionysus, however, was named for an ancient god of wine, parties and leisure. It was a cruise ship, showing off our expansion in, what we believed to be, uninhabited space. It had touched down on several verdant planets, simply showing them off to their passengers. I, was not on that ship. My wife, son, and daughter all were.\"

Dylan paused.

\"The Dionysus was the ship that you shot down. There's an expression, old as time as far as we can tell. 'An eye for an eye makes the whole world blind.' Long ago, we had wars. Fights over territory. Food. Water. Resources. We damn near killed ourselves off. I'd like to think we rose past that. The... impulsiveness of our past has been responsible for more atrocities than I care to go into. There's no reason for us to take revenge for impulsiveness. It's, tough. But I know that if I want to take revenge, then I'll destroy thousands of people's lives. I'd rather not be responsible for that.\"

Dylan looked up, his eyes passing between each of the other entities. Each seemed to be staring.

\"Now, if you don't mind. I need to get back to my ship. We have a meeting to setup.\"

Dylan stood and walked to the airlock. The rest stared at him as he left.
    """)

with open('bar.txt') as file:
    print(file.read())