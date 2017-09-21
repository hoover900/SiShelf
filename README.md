# SiShelf [Var.1.7.1]

! [SiShelf] (/ images / 01.png)

A shelf tool for Maya created by respecting Softimage's shelf.  
You can customize appearance and arrange freely, you can create your own shelf over the standard shelf tool.  
It can also be used as a floating window as well as docked in the Maya main window.  
If you use XPOP mode you will be able to do smooth work without occupying the screen area.

## Transition procedure from version 1.0 to 1.1 or later

Version 1.0 of the initial version described the code manually in userSetup.py, but from 1.1 it is enough to just place the folder in the specified location.
If you introduced 1.0, please move to 1.1 by the following procedure.  

1. Rename and move the data folder under the SiShelf [Var.1.0] folder to `C: \ Users \ user name \ Documents \ maya` as` SiShelf_data`.
2. Deleted the part added to userSetup.py.
3. Install Var.1.1 by the procedure of the following installation items

## Installation

1. Clone or download> Download Please download the ZIP file from ZIP.

2. Copy the unzipped SiShelf folder to `C: \ Program Files \ Autodesk \ ApplicationPlugins`.  
Even if Maya is installed on a drive other than drive C, it seems that SiShelf folder needs to be placed in `C: \ Program Files \ Autodesk \ ApplicationPlugins`.  
If you get confused, please put it in the same place as the bonus tool.


+ Create ApplicationPlugins folder if it does not exist.

+ It corresponds to multiple versions of Maya. In version 2014 and later, it is recognized automatically and the tool is ready to use.

+ Delete the folder if it becomes unnecessary.

+ It is safe to delete the SiShelf folder once, not overwrite when upgrading.

## Execution

It is possible to open it from main menu> Windows> SiShelf. You can also assign hot keys from Hotkey Editor> Custom Scripts> SiShelf.  

! [SiShelf] (/ images / 09.png)


## How to use

### Docking to the Maya window

SiShelf can dock in Maya's window.  
When you exit Maya with docking, the state is saved and Maya will start up in the next docked state.  

! [SiShelf] (/ images / 04.png)

### XPOP mode

It is a mode to display items registered in the shelf as compact menus.  
The shelf does not care about occupying the screen area! I recommend you to those who say.  
Since the menu is displayed at the position of the mouse cursor, if you register it as a hot key it will be able to do smooth work.
If you set the code of the hot key yourself, you can display only the contents of a specific tab.  
For details, refer to the item "Execute from code".

! [SiShelf] (/ images / 12.png)

Icons etc are also registered on the shelf will be displayed.  
By default, XPOP is displayed in the order in which buttons were created.  
If you want to change this, please set from the context menu XPOP Setting in shelf mode.

! [SiShelf] (/ images / 15.gif)

You can set the display order, whether or not to display, and whether or not to put the spacer in between.

You can customize appearance from Shelf 's context menu> Option.  

! [SiShelf] (/ images / 16.gif)

Please change to the appearance of your choice.  
If you uncheck Customize you can also make it look like a standard.

### Registering Buttons

There are two ways to register the tool on the shelf as follows.

+ Select text and drag and drop it to the shelf
+ Drag & drop files to shelf (.mel file, corresponding to .py file)

! [SiShelf] (/ images / 02.png)

Since the setting window of the button is displayed, enter arbitrary information and press OK to create the button.  
※ Labels and tool tips are reflected in the preview when the focus goes out of line feed or input field (to avoid bugs)

! [SiShelf] (/ images / 03.gif)


You can run the script with left mouse click.  
It is executed at the moment you talked, not at the moment of pressing the mouse.  
Execution can be canceled if the release position is set outside the button.


#### menu button

By specifying the button type as Menu Button, you can create buttons that can execute multiple commands.  
It is easy to understand by registering scripts etc. which are slightly different only once, so I think that it will help to save space.

! [SiShelf] (/ images / 11.gif)

You can edit labels by double clicking.  
It becomes a dividing line to arrange four or more half width hyphens (-).

### Partition line

You can add a divider line for organization in the tab.
You can freely set the presence / absence, color, etc. of portrait, sideways and labels.  
※ The label will be reflected in the preview when the focus deviates from the entry field (to avoid bugs)

! [SiShelf] (/ images / 05.gif)


### tab

You can add, delete, and rename tabs from the context menu of the mouse right click.  
Tab order can be changed by dragging.  
It is possible to set tab height and font size from Option in the context menu.  

! [SiShelf] (/ images / 06.gif)

### Reference Tab

It is possible to set to reference a specific tab from an external file from the External reference of the mouse right-click context menu.  
By using the reference tab, you can think of advantages such as being able to use tools common to many people such as teams and inside the company.

! [SiShelf] (/ images / 14.gif)

Please use the tab export function for the data to be read.  
Icons are displayed on the tabs on the reference tab, and you can not edit the contents.

### operation

Parts can be arranged and moved by dragging in the mouse.

! [SiShelf] (/ images / 07.gif)

You can select rectangle the part registered to the shelf with the left mouse drag.
With multiple selections, you can move all at once by middle mouse button dragging, delete from the context menu, etc.  
There are also commands which are not compatible with multiple selection at present.

! [SiShelf] (/ images / 08.gif)

### Snap function

You can enable the snap function from Shelf's context menu> Option.

! [SiShelf] (/ images / 10. gif)

You can specify the vertical and horizontal snap intervals, and display the guide grid when snapping.


### Context Menu

You can display the context menu by right-clicking the mouse.

Menu | Overview
----------- | --------------
 Add button | Add button
Add partition | Add a divider.
Edit | Edit the contents of the selected part. (Multiple selection is not supported.)
Delete | Deletes the selected part.
Copy | Copy the selected part. (Multiple selection is not supported.)
Paste | Paste the copied part to the clicked position.
Cut | Cut the selected part. (Multiple selection is not supported.)
Add Tab> Add | tab.
Tab> Rename | Changes the name of the current tab.
Tab> Delete | Deletes the current tab. Deleting the tab also deletes all part information that was placed on the tab.
Tab> Export | Writes information on the current tab to an external file.
Tab> Import | Read data from the external file to the current tab. Parts such as existing buttons are deleted.
Tab> External reference | Switches the current tab to the reference tab.
Tab> Remove external reference | Cancels the reference tab.
Default setting> Button | Performs initial settings when creating buttons.
Default setting> Partition | Perform initial settings when creating divider lines.
XPOP ​​Setting | Performs display settings such as the order to display in XPOP.
Option | Set options for the shelf.
Version information | Version information can be confirmed.

### Saving data

The data in the shelf is automatically saved at the timing of operations such as adding, deleting, moving parts.  
Currently there is no undo function. be careful.  

Data is created as json file in `C: \ Users \ user name \ Documents \ maya`.  
Since the json file is a text file, manual rewriting is also possible by changing the contents and saving it if you want to do.  
The same data is also referenced from multiple versions of Maya. Currently there is no referencing destination changing function due to version difference.


Run from ## code

When executing from code, it is as follows. (Paste and paste the code above into the script editor (Python tab))

### Shelf window display

Simple code example
`` `python
   import sishelf.shelf
   sishelf.shelf.main ()

`` `

The floating shelf window is displayed.

Argument name | Argument type | Default value | Overview
------------ | ------------ | ------------ | ------------ | --------------
x | int | None | window display X position (center when screen is omitted)
y | int | None | window display Y position (center when screen is omitted)
load_file | string | None | Specify the file path of the read data (also used as the save path)
edit_lock | boolean | False | Whether or not to lock the editing function (saving is not done in case of True)


### Shelf window display (mouse position)

Simple code example
`` `python
   import sishelf.shelf  
   sishelf.shelf.popup ()  
`` `


### XPOP mode

Simple code example
`` `python
   import sishelf.xpop  
   sishelf.xpop.main ()  
`` `

Argument name | Argument type | Default value | Overview
------------ | ------------ | ------------ | ------------ | --------------
tab | string | None | Makes the first hierarchy of XPOP the contents of the specified tab (if not specified, the tab name is the first hierarchy of XPOP)
load_file | string | None | Specify the file path of the read data


! [SiShelf] (/ images / 13.png)

## Operation confirmation

MAYA2014: I do not get up with a bug

MAYA 2015: No problem

MAYA2016: No problem

MAYA2017: No problem


### Understanding the problem

When the button Eidt window is displayed with + MAYA2017, the background color designation is not reflected (reflected when UI is manually updated)
+ When XPOP mode is assigned to a hot key, the displayed menu may remain if you call it continuously.


## Revision history

2017/4/30
+ Version 1.7.1
Implementation of appearance customization function of + XPOP

2017/4/28
+ Version 1.7.0
+ [Shelf] XPOP display setting function implementation
+ [XPOP] Fix to reflect display settings on shelf

2017/4/26
+ Version 1.6.0
+ [Shelf] tab exporting and loading function implementation
+ Reference of [Shelf / XPOP] tab (external reference) mode Implementation

2017/4/26
+ Version 1.5.3
+ Fixed a bug where the menu button, XPOP did not work properly when there were double-byte characters in the code

2017/4/25
+ Version 1.5.2
Fixed a bug that the character did not return after pressing the + button once

2017/4/25
+ Version 1.5.1
Both + shelf and XPOP add arguments to the call command. [Shelf] Specification of reading data, locking of editing function [XPOP] Specifying reading data, display Tab designation of the first hierarchy

2017/4/24
+ Version 1.5
+ XPOP mode addition

2017/4/23
+ Version 1.4
+ Supports menu button type.
+ Add tab character and height setting
+ Add version information to context menu

2017/4/20
+ Version 1.3.1
+ 2017 Compatible with restoration of docking state at startup

2017/4/17
+ Version 1.3
+ Corresponds to real-time preview of part movements of drag in mouse (placement becomes easier to intuitive)
+ Implement snap function
+ Fine adjustment so that intuitive parts selection function by clicking in the mouse, right click

2017/4/15
+ Version 1.2
Corresponds to the label color specification of the + button
Changed the specification so that it executes the code at the moment of clicking the + button at the moment you release it. Also, responds so that you can cancel it when you release it outside the button.


2017/4/13
+ Version 1.1.1
+ Delete unnecessary PYTHONPATH setting. Change internal imports to explicit relative import
+ Fixed bug that old data remained when editing parts in tab
+ Corresponds to the problem that Maya crashes depending on the environment while entering double-byte characters on labels and tooltips (It gets reflected when focus goes out)

2017/4/12
+ Version 1.1
It corresponds to + PackageContents.xml format.
+ Automatic registration of information in menu and hotkey editor
- Fixed that application of background color was not performed normally after editing button
+ Button Fixed a bug where the background color was not reflected when previewing the edit screen
+ Fixed the problem which caused error when file throwing to the shelf with MAYA2017
+ Others for fine detail MAYA2017

2017/4/10  
Fixed a bug where button background color specification was disabled in Maya 2016
+ Added note when downloading zip from github in "Preparation" item

2017/4/9  
+ Version 1.0 Published


## license

[MIT] (https://github.com/mochio326/SiShelf/blob/master/LICENSE)
