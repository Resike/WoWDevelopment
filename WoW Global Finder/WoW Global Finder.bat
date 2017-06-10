@echo off
pushd %~dp0
luac-wow -l -p %1 | lua-wow Globals.lua %1
