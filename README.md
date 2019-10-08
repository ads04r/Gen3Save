Gen3Save
========

A Python library for parsing a Gameboy Advance Pokemon Gen III save file.

Call the script from the command line with

    python pokemondata/Gen3Save.py savefile.sav

Use from within python with

    from pokemondata import Gen3Save
    
    data = Gen3Save('savefile.sav')

where savefile.sav is a Gen III save file, obtainable either by playing a Gen
III game via an emulator such as VisualBoy Advance, or by transferring the
save data directly from a Gameboy Advance cartridge. You can find a guide
to doing this here:

https://www.drashsmith.com/post/copying-save-files-from-gameboy-advance-games-to-a-pc/

Documentation
-------------

There are two classes, Gen3Save and Gen3Pokemon. The whole thing is read-only
so you should have no need to create a Gen3Pokemon class, these can be
obtained from the Gen3Save class. Once you've loaded your save file, you
can get the pokemon out of it using the following properties

* `team`  returns a list containing the pokemon in the player's party.
* `boxes` returns a list containing all the pokemon in Lanette's PC.

The pokemon class has the following properties

* `name` returns the pokemon's nickname (or species name if none) as a string.
* `trainer` returns an object containing the trainer ID and name of the pokemon's original trainer.
* `level` returns the pokemon's level, as an integer.
* `species` returns an object containing the pokemon's species, and information relating to it.
* `nature` returns the pokemon's nature as a string.
* `moves` returns a list of objects, each referring to a move the pokemon knows.
* `exp` returns the pokemon's EXP level, as an integer.
* `ivs` this is basically unfinished - it returns (some of) the pokemon's individual data. I'll finish it one day.

There is also a lower-level property...

* `data` returns the pokemon data, unencrypted, which can be saved in a PKM file, compatible with A-Save.

Credits / Thanks
----------------

This library would not be possible without these documents on Bulbapedia...

* https://m.bulbapedia.bulbagarden.net/wiki/Save_data_structure_in_Generation_III
* https://m.bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_in_Generation_III
* https://m.bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_substructures_in_Generation_III
* https://m.bulbapedia.bulbagarden.net/wiki/Character_encoding_in_Generation_III

Whoever did the reverse engineering and writing up of the save format, thank you.


Why Gen III?
------------

Several reasons...

* It's trivial to get save data off a GBA cart and into a PC
* Gen III is the point at which the data format got interesting
* Pokemon caught in Gen III can be traded right up to Gen VII
* Gen IV is crap (bite me)
