# General Converter (Flow.Launcher.GenConvert)

General weight, distance, area, temperature converter for the [Flow Launcher](https://github.com/Flow-Launcher/Flow.Launcher)

### About

### Requirements

Python 3.5 or later installed on your system, with python.exe in your PATH variable and this path updated in the Flow Launcher settings (this is a general requirement to use Python plugins with Flow). As of v1.8, Flow Launcher should take care of the installation of Python for you if it is not on your system.

### Installing

#### Package Manager

Use the `pm install` command from within Flow itself

#### Manual

Add the Flow.Launcher.Plugin.GenConvert directory to %APPDATA%\Roaming\FlowLauncher\Plugins\ and restart Flow.

### Localisation

Currently English and Chinese language supported. Edit the .env file to change the language.

### Usage

| Keyword                             | Description                                        |
| ----------------------------------- | -------------------------------------------------- |
| `gc <amount> <from unit> <to unit>` | Convert the amount of the from unit to the to unit |

#### Units

The following units and their abbreviations can be used (each table can only convert among its' own units):

<table>
  <tr>
    <th>Subject</th>
    <th>Unit</th>
    <th>Abbreviation</th>
  </tr>
  <tr>
    <td rowspan="8" align="center">Distance</td>
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
  </tr>
  <tr>
    <td rowspan="9" align="center">Fluids</td>
    <td>millilitre</td>
    <td>ml</td>
   </tr>
  <tr>
    <td>litre</td>
    <td>l</td>
  </tr>
  <tr>
    <td>pint</td>
    <td>pt</td>
  </tr>
  <tr>
    <td>quart</td>
    <td>qt</td>
  </tr>
  <tr>
    <td>cup</td>
    <td>cup</td>
  </tr>
  <tr>
    <td>teaspoon</td>
    <td>tsp</td>
  </tr>
  <tr>
    <td>tablespoon</td>
    <td>tbsp</td>
  </tr>
  <tr>
    <td>gallon</td>
    <td>gal</td>
  </tr>
  <tr>
    <td>gram</td>
    <td>gm</td>
  </tr>
</table>

<table>
  <tr>
    <th>Subject</th>
    <th>Unit</th>
    <th>Abbreviation</th>
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
  </tr>
  <tr>
    <td rowspan="6" align="center">Weight</td>
    <td>gram</td>
    <td>gm</td>
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
  </tr>
  <tr>
    <td rowspan = "2" align="center">Temperature</td>
    <td>celsius</td>
    <td>c</td>
   </tr>
  <tr>
    <td>Farenheit</td>
    <td>f</td>
  </tr>
</table>

### Problems, errors and feature requests

Open an issue in this repo.
