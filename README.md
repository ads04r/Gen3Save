Gen3Save
========

A Python library for parsing a Gameboy Advance Pokemon Gen III save file.

Call the script from the command line with

    python pokemondata/Gen3Save.py savefile.sav

Use from within python with

    from pokemondata import Gen3Save
    
    data = Gen3Save('savefile.sav')



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
* Gen IV is crap

