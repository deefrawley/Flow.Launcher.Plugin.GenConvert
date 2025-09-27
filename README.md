[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# General Converter (Flow.Launcher.GenConvert)

General weight, volume, distance, area, temperature, speed and energy converter for the [Flow Launcher](https://github.com/Flow-Launcher/Flow.Launcher)

### About

### Requirements

Python 3.9 or later. As of Flow Launcher v1.8, Flow should take care of the installation of Python for you if it is not on your system.

### Installing

#### Package Manager

Use the `pm install` command from within Flow itself

#### Manual

Add the Flow.Launcher.Plugin.GenConvert directory to %APPDATA%\Roaming\FlowLauncher\Plugins\ and restart Flow.

### Localisation

Currently English and Chinese language supported. Edit the .env file to change the language.

### Usage

| Keyword                                                       | Description                                         |
| ------------------------------------------------------------- | --------------------------------------------------- |
| `gc <amount> <from unit abbreviation> <to unit abbreviation>` | Convert the amount of the from unit to the to unit. |

The from and to unit are case sensitive.

Just entering the keyword will give you the full list of units to choose from in Flow. If you want to remove the keyword for this plugin and have it return
results when you simply start entering a number then go to the Plugin settings and turn this helper text off.

Entering the keyword, amount and from unit will give you a subset list of units the from unit can be converted to

#### Units

The following units and their abbreviations can be used (each table can only convert among its' own units):

<table>
  <tr>
    <th>Subject</th>
    <th>Unit</th>
    <th>Abbreviation</th>
    <th rowspan="10" align="center"><img src="assets/Distance.ico" alt="Distance Logo"></th>
  </tr>
  <tr>
    <td rowspan="9" align="center"> Distance</td>
    <td>millimetre</td>
    <td>mm</td>
  </tr>
  <tr>
    <td>centimetre</td>
    <td>cm</td>
  </tr>
  <tr>
    <td>metre</td>
    <td>m</td>
  </tr>
  <tr>
    <td>decimetre</td>
    <td>dm</td>
  </tr>
  <tr>
    <td>kilometre</td>
    <td>km</td>
  </tr>
  <tr>
    <td>inch</td>
    <td>in</td>
  </tr>
  <tr>
    <td>foot/feet</td>
    <td>ft</td>
  </tr>
  <tr>
    <td>yard</td>
    <td>yd</td>
  </tr>
  <tr>
    <td>mile</td>
    <td>mi</td>
  </tr>
</table>

<table>
  <tr>
    <th>Subject</th>
    <th>Unit</th>
    <th>Abbreviation</th>
    <th rowspan="27" align="center"><img src="assets/Volume.ico" alt="Volume Logo"></th>
  </tr>
  <tr>
    <td rowspan="26" align="center">Volume</td>
    <td>millilitre</td>
    <td>ml</td>
  </tr>
  <tr>
    <td>gram</td>
    <td>g</td>
  </tr>
  <tr>
    <td>litre</td>
    <td>l</td>
  </tr>
  <tr>
    <td>decalitre</td>
    <td>decal</td>
  </tr>
  <tr>
    <td>pint US</td>
    <td>pt</td>
  </tr>
  <tr>
    <td>pint Imperial</td>
    <td>ptimp</td>
  </tr>
  <tr>
    <td>quart US</td>
    <td>qt</td>
  </tr>
  <tr>
    <td>quart Imperial</td>
    <td>qtimp</td>
  </tr>
  <tr>
    <td>cup US</td>
    <td>cup</td>
  </tr>
  <tr>
    <td>cup Imperial</td>
    <td>cupimp</td>
  </tr>
  <tr>
    <td>teaspoon US</td>
    <td>tsp</td>
  </tr>
  <tr>
    <td>teaspoon Imperial</td>
    <td>tspimp</td>
  </tr>
  <tr>
    <td>tablespoon US</td>
    <td>tbsp</td>
  </tr>
  <tr>
    <td>tablespoon Imperial</td>
    <td>tbspimp</td>
  </tr>
  <tr>
    <td>gallon US</td>
    <td>gal</td>
  </tr>
  <tr>
    <td>gallon Imperial</td>
    <td>galimp</td>
  </tr>
  <tr>
    <td>fluid ounce US</td>
    <td>floz</td>
  </tr>
  <tr>
    <td>fluid ounce Imperial</td>
    <td>flozimp</td>
  </tr>
  <tr>
    <td>cubic decimetre</td>
    <td>dm3</td>
  </tr>
  <tr>
    <td>cubic millimetre</td>
    <td>mm3</td>
  </tr>
  <tr>
    <td>cubic centimetre</td>
    <td>cm3</td>
  </tr>
  <tr>
    <td>cubic metre</td>
    <td>m3</td>
  </tr>
  <tr>
    <td>cubic inch</td>
    <td>in3</td>
  </tr>
  <tr>
    <td>cubic feet</td>
    <td>ft3</td>
  </tr>
  <tr>
    <td>bushel UK</td>
    <td>buuk</td>
  </tr>
  <tr>
    <td>bushel US</td>
    <td>buus</td>
  </tr>
</table>

<table>
  <tr>
    <th>Subject</th>
    <th>Unit</th>
    <th>Abbreviation</th>
    <th rowspan="10" align="center"><img src="assets/Area.ico" alt="Area Logo"></th>
  </tr>
  <tr>
    <td rowspan="9" align="center">Area</td>
    <td>square metre</td>
    <td>sqm</td>
   </tr>
  <tr>
    <td>square centremetre</td>
    <td>sqcm</td>
  </tr>
  <tr>
    <td>square kilometre</td>
    <td>sqkm</td>
  </tr>
  <tr>
    <td>square inch</td>
    <td>sqin</td>
  </tr>
  <tr>
    <td>square foot</td>
    <td>sqft</td>
  </tr>
  <tr>
    <td>square mile</td>
    <td>sqmi</td>
  </tr>
  <tr>
    <td>square yard</td>
    <td>sqyd</td>
  </tr>
  <tr>
    <td>hectare</td>
    <td>h</td>
  </tr>
  <tr>
    <td>acre</td>
    <td>ac</td>
  </tr>
</table>

<table>
  <tr>
    <th>Subject</th>
    <th>Unit</th>
    <th>Abbreviation</th>
    <th rowspan="7" align="center"><img src="assets/Weight.ico" alt="Weight Logo"></th>
  </tr>
  <tr>
    <td rowspan="6" align="center">Weight</td>
    <td>gram</td>
    <td>g</td>
   </tr>
  <tr>
    <td>kilogram</td>
    <td>kg</td>
  </tr>
  <tr>
    <td>pound</td>
    <td>lb</td>
  </tr>
  <tr>
    <td>ounce</td>
    <td>oz</td>
  </tr>
  <tr>
    <td>stone</td>
    <td>st</td>
  </tr>
  <tr>
    <td>ton</td>
    <td>ton</td>
  </tr>
</table>

<table>
  <tr>
    <th>Subject</th>
    <th>Unit</th>
    <th>Abbreviation</th>
    <th rowspan="4" align="center"><img src="assets/Temperature.ico" alt="Temperature Logo"></th>
  </tr>
  <tr>
    <td rowspan = "3" align="center">Temperature</td>
    <td>celsius</td>
    <td>c</td>
   </tr>
  <tr>
    <td>Farenheit</td>
    <td>f</td>
  </tr>
  <tr>
    <td>Kelvin</td>
    <td>k</td>
  </tr>
</table>

<table>
  <tr>
    <th>Subject</th>
    <th>Unit</th>
    <th>Abbreviation</th>
    <th rowspan="4" align="center"><img src="assets/Speed.ico" alt="Speed Logo"></th>
  </tr>
  <tr>
    <td rowspan = "3" align="center">Speed</td>
    <td>kilometres per hour</td>
    <td>km/h</td>
   </tr>
  <tr>
    <td>miles per hour</td>
    <td>mp/h</td>
  </tr>
  <tr>
    <td>knots</td>
    <td>kt</td>
  </tr>
</table>

<table>
  <tr>
    <th>Subject</th>
    <th>Unit</th>
    <th>Abbreviation</th>
    <th rowspan="8" align="center"><img src="assets/Energy.ico" alt="Energy Logo"></th>
  </tr>
  <tr>
    <td rowspan = "7" align="center">Energy</td>
    <td>calories</td>
    <td>cal</td>
   </tr>
  <tr>
    <td>kilocalories</td>
    <td>kcal</td>
  </tr>
  <tr>
    <td>kilojoules</td>
    <td>kJ</td>
  </tr>
  <tr>
    <td>megajoules</td>
    <td>MJ</td>
  </tr>
  <tr>
    <td>gigajoules</td>
    <td>Gj</td>
  </tr>
  <tr>
    <td>kilowatt hours</td>
    <td>kWh</td>
  </tr>
  <tr>
    <td>British thermal units</td>
    <td>BTU</td>
  </tr>
<table>
  <tr>
    <th>Subject</th>
    <th>Unit</th>
    <th>Abbreviation</th>
    <th rowspan="13" align="center"><img src="assets/Data.ico" alt="Data Logo"></th>
  </tr>
  <tr>
    <td rowspan = "13" align="center">Data</td>
    <td>Bytes</td>
    <td>B</td>
   </tr>
  <tr>
    <td>KiloBytes</td>
    <td>KB</td>
  </tr>
  <tr>
    <td>GigaBytes</td>
    <td>GB</td>
  </tr>
  <tr>
    <td>PetaBytes</td>
    <td>PB</td>
  </tr>
  <tr>
    <td>Kibibytes</td>
    <td>KiB</td>
  </tr>
  <tr>
    <td>Gibibytes</td>
    <td>GiB</td>
  </tr>
  <tr>
    <td>Pebibytes</td>
    <td>PiB</td>
  </tr>
  <tr>
    <td>bits</td>
    <td>b</td>
  </tr>
  <tr>
    <td>Kilobits</td>
    <td>Kb</td>
  </tr>
  <tr>
    <td>Megabits</td>
    <td>Mb</td>
  </tr>
  <tr>
    <td>Gigabits</td>
    <td>Gb</td>
  </tr>
  <tr>
    <td>Terabits</td>
    <td>Tb</td>
  </tr>
  <tr>
    <td>Pebibytes</td>
    <td>PiB</td>
  </tr>
</table>

### Problems, errors and feature requests

Open an issue in this repo.
