# [GCE Eco-Devices RT2](http://gce-electronics.com/fr/home/1345-suivi-consommation-ecodevices-rt2-3760309690049.html) component for [Home Assistant](https://www.home-assistant.io/)

This a *custom component* for [Home Assistant](https://www.home-assistant.io/) for [GCE Eco-Devices RT2](http://gce-electronics.com/fr/home/1345-suivi-consommation-ecodevices-rt2-3760309690049.html).
This work is based on the work of [Aohzan](https://github.com/Aohzan/ecodevices).

If you have:
- [GCE Eco-Devices RT2](http://gce-electronics.com/fr/home/1345-suivi-consommation-ecodevices-rt2-3760309690049.html), this repository is for you.
- [GCE Eco-Devices](http://gce-electronics.com/fr/carte-relais-ethernet-module-rail-din/409-teleinformation-ethernet-ecodevices.html), see the great work of [Aohzan](https://github.com/Aohzan/ecodevices)


## Sensors and [Eco-Devices RT2 API](https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf)

It is a simple way to call the API of the Eco-Devices RT2 defined [here](https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf).

## Configuration
### Installation

Copy the `ecodevices` folder to you `custom_components` folder and restart Home Assistant.

### Simple Example -- Sensor
See [Eco-Devices RT2 API](https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf) for details of `_COMMAND_`, `_VALUE_` parameter, and test the resquest in your web browser for `_ENTRY_`.
```yaml
# Example configuration.yaml entry, which will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&_COMMAND_=_VALUE_ and get _ENTRY_ in the JSON response. 
sensor:
  - platform: ecodevices
    host: "_ADDRESS_IP_"
    port: _PORT_   
    api_key: "_API_KEY_"
    scan_interval: 5
    name: _SENSOR_NAME_IN_HA_
    rt2_command: "_COMMAND_"
    rt2_command_value: "_VALUE_"
    rt2_command_entry: "_ENTRY_"
    unit_of_measurement: "kW"
    device_class: "power"
```

For example, to get "Index_TI1" which is the first "Télé-Information", the "HC Index".
```yaml
# Example configuration.yaml entry, which will call http://192.168.0.20:80/api/xdevices.json?key=XxLzMY69z&Index=All and get "Index_TI1" in the JSON response.
sensor:
  - platform: ecodevices
    host: "192.168.0.20"
    port: 80    
    api_key: "XxLzMY69z"
    scan_interval: 5
    name: Elec Index HC
    rt2_command: "Index"
    rt2_command_value: "All"
    rt2_command_entry: "Index_TI1"
    unit_of_measurement: "kWh" # default=W
    device_class: "power" # default=power
    icon: "mdi:flash" # default=mdi:flash
```

### Simple Example -- Switch
See [Eco-Devices RT2 API](https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf) for details of `_COMMAND_`, `_PARAMETER_` parameter, and test the resquest in your web browser for `_NAME_`.
```yaml
# Example configuration.yaml entry.
# 1- VALUE -- To check the current value of the switch, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&_COMMAND_=_VALUE_ and get _ENTRY_ in the JSON response.
# 2- ON -- To change the current value of the switch to ON, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&_ON_COMMAND_=_ON_VALUE_ and it will check if the "status" in the JSON response is equal to "Success".
# 3- OFF -- To change the current value of the switch to OFF, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&_OFF_COMMAND_=_OFF_VALUE_ and it will check if the "status" in the JSON response is equal to "Success".
switch:
  - platform: ecodevices
    host: "_ADDRESS_IP_"
    port: _PORT_   
    api_key: "_API_KEY_"
    scan_interval: 5
    name: _SWITCH_NAME_IN_HA_
    rt2_command: "_COMMAND_"
    rt2_command_value: "_VALUE_"
    rt2_command_entry: "_ENTRY_"
    rt2_on_command: "_ON_COMMAND_"
    rt2_on_command_value: "_ON_VALUE_"
    rt2_off_command: "_OFF_COMMAND_"
    rt2_off_command_value: "_OFF_VALUE_"
    device_class: "switch"  # default=switch
    icon: "mdi:toggle-switch" # default=mdi:toggle-switch
```

For example, to play with the first EnOcean swith.
```yaml
# 1- VALUE -- To check the current value of the switch: http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=XxLzMY69z&Get=XENO and get "ENO ACTIONNEUR1" in the JSON response.
# 2- ON -- To change the current value of the switch to ON: http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=XxLzMY69z&SetEnoPC=1 and it will check if the "status" in the JSON response is equal to "Success".
# 3- OFF -- To change the current value of the switch to OFF: http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=XxLzMY69z&ClearEnoPC=1 and it will check if the "status" in the JSON response is equal to "Success".
switch:
  - platform: ecodevices
    host: "192.168.0.20"
    port: 80    
    api_key: "XxLzMY69z"
    scan_interval: 5
    name: First EnOcean Switch
    rt2_command: "Get"
    rt2_command_value: "XENO"
    rt2_command_entry: "ENO ACTIONNEUR1"
    rt2_on_command: "SetEnoPC"
    rt2_on_command_value: "1"
    rt2_off_command: "ClearEnoPC"
    rt2_off_command_value: "1"
    device_class: "switch"
    icon: "mdi:toggle-switch"
```

### Full Example
```yaml
# Example configuration.yaml entry
sensor:
  # Get Elec Index HC
  - <<: &ecodevices
      platform: ecodevices
      host: "192.168.0.20"
      port: 80    
      api_key: "XxLzMY69z"
      scan_interval: 5
    name: Elec Index HC
    rt2_command: "Index"
    rt2_command_value: "All"
    rt2_command_entry: "Index_TI1"
    unit_of_measurement: "kWh"
    device_class: "energy"
  # Get Elec Index HP
  - <<: *ecodevices
    name: Elec Index HP
    rt2_command: "Index"
    rt2_command_value: "All"
    rt2_command_entry: "Index_TI2"
    unit_of_measurement: "kWh"
    device_class: "energy"
  # Compute Elec Index, sum of (Elec Index HP) and (Elec Index HC)
  - platform: template
    sensors:
      elec_index:
        friendly_name: "Elec Index"
        unit_of_measurement: "kWh"
        icon_template: "mdi:flash"
        device_class: "energy"
        value_template: "{{ states('sensor.elec_index_hp') | float + states('sensor.elec_index_hc') | float }}"
  # Get Elec HP/HC (If your are currently in HP or HC hours, according to your electrical counter)
  - <<: *ecodevices
    name: Elec HP/HC
    rt2_command: "Get"
    rt2_command_value: "TI"
    rt2_command_entry: "PTEC"
    unit_of_measurement: ""
    device_class: "None"
  # Get Elec Puissance Appelée
  - <<: *ecodevices
    name: Elec Puissance Appelée
    rt2_command: "Get"
    rt2_command_value: "P"
    rt2_command_entry: "INSTANT_POSTE1"
    unit_of_measurement: "kW"
    device_class: "power"



switch:
  - <<: *ecodevices
  # Get value and change the first EnOcean Switch
    name: First EnOcean Switch
    rt2_command: "Get"
    rt2_command_value: "XENO"
    rt2_command_entry: "ENO ACTIONNEUR1"
    rt2_on_command: "SetEnoPC"
    rt2_on_command_value: "1"
    rt2_off_command: "ClearEnoPC"
    rt2_off_command_value: "1"
    device_class: "switch"
    icon: "mdi:toggle-switch"
```
