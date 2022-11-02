[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# General Converter (Flow.Launcher.GenConvert)

General weight, volume, distance, area, temperature converter for the [Flow Launcher](https://github.com/Flow-Launcher/Flow.Launcher)

### About

### Requirements

Python 3.5 or later. As of Flow Launcher v1.8, Flow should take care of the installation of Python for you if it is not on your system.

### Installing

#### Package Manager

Use the `pm install` command from within Flow itself

#### Manual

Add the Flow.Launcher.Plugin.GenConvert directory to %APPDATA%\Roaming\FlowLauncher\Plugins\ and restart Flow.

### Localisation

Currently English and Chinese language supported. Edit the .env file to change the language.

### Usage

| Keyword                                                       | Description                                        |
| ------------------------------------------------------------- | -------------------------------------------------- |
| `gc <amount> <from unit abbreviation> <to unit abbreviation>` | Convert the amount of the from unit to the to unit. |

Just entering the keyword will give you the full list of units to choose from in Flow.

Entering the keyword, amount and from unit will give you a subset list of units the from unit can be converted to
#### Units

The following units and their abbreviations can be used (each table can only convert among its' own units):

<table>
  <tr>
    <th>Subject</th>
    <th>Unit</th>
    <th>Abbreviation</th>
    <th rowspan="9" align="center"><img src="assets/Distance.ico" alt="Distance Logo"></th>
  </tr>
  <tr>
    <td rowspan="8" align="center"> Distance</td>
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
    <th rowspan="189" align="center"><img src="assets/Volume.ico" alt="Volume Logo"></th>
  </tr>
  <tr>
    <td rowspan="17" align="center">Volume</td>
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

### Problems, errors and feature requests

Open an issue in this repo.
