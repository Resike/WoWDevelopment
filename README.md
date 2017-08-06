# WoWDevelopment
World of Warcraft Syntax Highlight and Auto-Completion for Sublime Text 2/3.

![](http://i.imgur.com/4f65dfl.png)

# Features:

* Full API syntax highlighting for lua, xml and toc files.
* Global finder build system, which finds any global variables with detailed information for the current lua file.

# Installation:
* Download the package, unzip it then remove the *-master* suffix, and copy the folder into your Sublime Text 2/3 Packages folder.
* Open any of the supported file and set the syntax for the selected file: WoWDevelopment -> WoW Lua, WoW TOC, WoW XML.

The autocomplete is based on scopes, so no settings are neccessary.

# List globals with a build system in the console window with detailed information:
* In Sublime *Tools -> Build System ->* Select *Wow Global Finder*.
* *Ctrl+B* to run the system.

  # Adding globals to ignore for the build system:
  * Add a commented line in the *lua* file and list the globals with commas: -- GLOBALS: math, string, table

# How to highlight globals with Sublime Linter:
* First install the SublimeLinter package.
* Then add the path to *luacheck.exe* to your system PATH table, or to the *paths/windows* setting in the Sublime Linter settings:
"c:\\Users\\UserName\\AppData\\Roaming\\Sublime Text 3\\Packages\\WoWDevelopment\\WoW Global Finder\\"
* Add *"wow lua": "lua",* to the *syntax_map* in the Sublime Linter settings.
![](http://i.imgur.com/Caqp3Aj.png)
* In Sublime *Tools -> SublimeLinter -> Toggle Linter* then enable *globalfinder* and disable any other installed linters.
* Restart Sublime.

  # Adding globals to ignore for luacheck in Sublime Linter:
  * Add a commented line in the *lua* file and list the globals without commas: -- luacheck: globals math string table

Ignored globals:
* Global Functions: *Reference\API Reference\API Reference (blizzard).sublime-completions.txt*
* Global Booleans: *Reference\Global Reference\Global Booleans.sublime-completions.txt*
* Global Console Variables: *Reference\Global Console Variables.sublime-completions.txt*
* Global Numbers: *Reference\Global Reference\Global Numbers.sublime-completions.txt*
* Global Strings: *Reference\Global Reference\Global Strings.sublime-completions.txt*

If you would like to enable autocomplete for these, just change the *.txt* extension to: *.sublime-completions*.
