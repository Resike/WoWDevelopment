# WoWDevelopment
World of Warcraft Syntax Highlight and Auto-Completion for Sublime Text 2/3.

# Features:

* Full API syntax highlighting for lua, xml and toc files.
* Global finder build system, which finds any global variables with detailed information for the current lua file.

# Installation:
* Download the package (remove the -master suffix), and copy the folder into your Sublime Text 2/3 Packages folder.
* Open any of the supported file and set the syntax for the selected file: WoWDevelopment -> WoW Lua, WoW TOC, WoW XML.

The autocomplete is based on scopes, so no settings are neccessary.

Ignored globals:
* Global Functions: *Reference\API Reference\API Reference (blizzard).sublime-completions.txt*
* Global Booleans: *Reference\Global Reference\Global Booleans.sublime-completions.txt*
* Global Numbers: *Reference\Global Reference\Global Numbers.sublime-completions.txt*

If you would like to enable autocomplete for these, just change the *.txt* extension to: *.sublime-completions*.