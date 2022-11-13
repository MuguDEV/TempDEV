# TempDEV

A Small Project made by me. For Conversion of Temperature from one [Temperature Scale](https://en.wikipedia.org/wiki/Scale_of_temperature) to Another

## Example

```Python
import TempDEV as TD

#Create an Object
temp = TD.Temperature_Converions()
temp.convert("c", 1, "j")
```

## Output

On Executing the above code it gives output as [JSON](https://www.json.org/json-en.html). like this

```Python
{
  "Celsius": -261.15,
  "Fahrenheit": -438.07,
  "Rankine": 21.6,
  "Delisle": 541.7249999999999
}

```

> Available Temperature Scales
 - Celsius
 - Fahrenheit
 - Kelvin
 - Rankine
 - Delisle

> Available Methods
 - convert(Scale, value, Return_Type)
 - symbols(scale)
 
Scale {c-Celsius, f-Fahrenheit, k-Kelvin, r-Rankine, d-Delisle}
Return {d-Dictionary, l-List, t-Tuple, s-Set, j-JSON}
 
> Update
  
  `Many Scales will added to this Project! Soon....`
