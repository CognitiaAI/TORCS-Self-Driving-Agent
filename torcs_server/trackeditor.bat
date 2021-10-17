@echo off
set TE_HOME=.

java -classpath "%TE_HOME%\trackeditor\lib\looks-1.2.2.jar";"%TE_HOME%\trackeditor\lib\jdom.jar";"%TE_HOME%\trackeditor\lib\xercesImpl.jar";"%TE_HOME%\trackeditor\lib\bsh-2.0b2.jar";"%TE_HOME%\trackeditor\lib\trackeditor-0.6.2c.jar"  utils.TrackEditor
