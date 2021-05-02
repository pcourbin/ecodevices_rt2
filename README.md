[![License][license-shield]](LICENSE)
[![Community Forum][forum-shield]][forum]

[![pre-commit][pre-commit-shield]][pre-commit]
[![Black][black-shield]][black]

[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

# [GCE Ecodevices RT2](http://gce-electronics.com/fr/home/1345-suivi-consommation-ecodevices-rt2-3760309690049.html) component for [Home Assistant](https://www.home-assistant.io/)

This is a _custom component_ for [Home Assistant](https://www.home-assistant.io/) for [GCE Ecodevices RT2](http://gce-electronics.com/fr/home/1345-suivi-consommation-ecodevices-rt2-3760309690049.html). This work is based on the work of [Aohzan](https://github.com/Aohzan/ecodevices).
It uses python package [pyecodevices-rt2](https://github.com/pcourbin/pyecodevices_rt2) to call the [Ecodevices RT2 API](https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf).

If you have:

- [GCE Ecodevices RT2](http://gce-electronics.com/fr/home/1345-suivi-consommation-ecodevices-rt2-3760309690049.html), this repository is for you.
- [GCE Ecodevices](http://gce-electronics.com/fr/carte-relais-ethernet-module-rail-din/409-teleinformation-ethernet-ecodevices.html), see the great work of [Aohzan](https://github.com/Aohzan/ecodevices)
- [GCE IPX800 V4](https://www.gce-electronics.com/fr/carte-relais-ethernet-module-rail-din/1483-domotique-ethernet-webserver-ipx800-v4-3760309690001.html), see the great work of [Aohzan](https://github.com/Aohzan/ipx800)

## Table of contents

- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Examples](#examples)
  - [Simple Example -- Sensor](#simple-example----sensor)
  - [Simple Example -- Switch](#simple-example----switch)
  - [Simple Example -- Climate](#simple-example----climate)
  - [Full Example](#full-example)

## Installation

Copy the `custom_components/ecodevices_rt2` folder into the config folder.

## Examples

### Simple Example -- Sensor

See [Ecodevices RT2 API](https://gce.ovh/wiki/index.php?title=API_EDRT) (or [PDF](https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf)) for details of `_COMMAND_`, `_VALUE_` parameters, and test the request in your web browser for `_ENTRY_`.

```yaml
# Example configuration.yaml entry, which will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&_COMMAND_=_VALUE_ and get _ENTRY_ in the JSON response.
sensor:
  - platform: ecodevices_rt2
    host: "_ADDRESS_IP_"
    port: _PORT_
    api_key: "_API_KEY_"
    scan_interval: 5
    friendly_name: _SENSOR_NAME_IN_HA_
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
  - platform: ecodevices_rt2
    host: "192.168.0.20"
    port: 80
    api_key: "XxLzMY69z"
    scan_interval: 5
    friendly_name: Elec Index HC
    rt2_command: "Index"
    rt2_command_value: "All"
    rt2_command_entry: "Index_TI1"
    unit_of_measurement: "kWh" # default=W
    device_class: "power" # default=power
    icon: "mdi:flash" # default=mdi:flash
```

### Simple Example -- Switch

See [Ecodevices RT2 API](https://gce.ovh/wiki/index.php?title=API_EDRT) (or [PDF](https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf)) for details of `_COMMAND_`, `_VALUE_` parameters, and test the request in your web browser for `_ENTRY_`.

```yaml
# Example configuration.yaml entry.
# 1- VALUE -- To check the current value of the switch, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&_COMMAND_=_VALUE_ and get _ENTRY_ in the JSON response.
# 2- ON -- To change the current value of the switch to ON, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&_ON_COMMAND_=_ON_VALUE_ and it will check if the "status" in the JSON response is equal to "Success".
# 3- OFF -- To change the current value of the switch to OFF, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&_OFF_COMMAND_=_OFF_VALUE_ and it will check if the "status" in the JSON response is equal to "Success".
switch:
  - platform: ecodevices_rt2
    host: "_ADDRESS_IP_"
    port: _PORT_
    api_key: "_API_KEY_"
    scan_interval: 5
    friendly_name: _SWITCH_NAME_IN_HA_
    rt2_command: "_COMMAND_"
    rt2_command_value: "_VALUE_"
    rt2_command_entry: "_ENTRY_"
    rt2_on_command: "_ON_COMMAND_"
    rt2_on_command_value: "_ON_VALUE_"
    rt2_off_command: "_OFF_COMMAND_"
    rt2_off_command_value: "_OFF_VALUE_"
    device_class: "switch" # default=switch
    icon: "mdi:toggle-switch" # default=mdi:toggle-switch
```

For example, to play with the first EnOcean switch.

```yaml
# 1- VALUE -- To check the current value of the switch: http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=XxLzMY69z&Get=XENO and get "ENO ACTIONNEUR1" in the JSON response.
# 2- ON -- To change the current value of the switch to ON: http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=XxLzMY69z&SetEnoPC=1 and it will check if the "status" in the JSON response is equal to "Success".
# 3- OFF -- To change the current value of the switch to OFF: http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=XxLzMY69z&ClearEnoPC=1 and it will check if the "status" in the JSON response is equal to "Success".
switch:
  - platform: ecodevices_rt2
    host: "192.168.0.20"
    port: 80
    api_key: "XxLzMY69z"
    scan_interval: 5
    friendly_name: First EnOcean Switch
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

### Simple Example -- Climate

See [Ecodevices RT2 API](https://gce.ovh/wiki/index.php?title=API_EDRT) (or [PDF](https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf)) for details of `_COMMAND_`, `_VALUE_` parameters, and test the request in your web browser for `_ENTRY_`.

```yaml
# Example configuration.yaml entry.
# 1- Get FP value -- To check the current value of the FP Zone, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&Get=FP and get "FP%s Zone %s" in the JSON response with first %s is _FP_EXTENTION_ and second %s is _FP_ZONE_
# 2- Set FP value -- To change the current value of the FP Zone to a specific mode, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&_COMMAND_=_VALUE_ with _COMMAND_="SetFP0%s" (%s is computed using _FP_EXTENTION_ and _FP_ZONE_), _VALUE_ is equal to the right mode (0 for CONFORT, 1 for ECO, 2 for AWAY and 3 for NONE) and it will check if the "status" in the JSON response is equal to "Success".
climate:
  - platform: ecodevices_rt2
    host: "_ADDRESS_IP_"
    port: _PORT_
    api_key: "_API_KEY_"
    scan_interval: 5
    friendly_name: _CLIMATE_NAME_IN_HA_
    rt2_fp_ext: "_FP_EXTENTION_"
    rt2_fp_zone: "_FP_ZONE_"
```

For example, to play with the first FP zone of the first extension.

```yaml
# Example configuration.yaml entry.
# 1- Get FP value -- To check the current value of the FP Zone, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&Get=FP and get "FP%s Zone %s" in the JSON response with first %s is _FP_EXTENTION_ and second %s is _FP_ZONE_
# 2- Set FP value -- To change the current value of the FP Zone to a specific mode, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&_COMMAND_=_VALUE_ with _COMMAND_="SetFP0%s" (%s is computed using _FP_EXTENTION_ and _FP_ZONE_), _VALUE_ is equal to the right mode (0 for CONFORT, 1 for ECO, 2 for AWAY and 3 for NONE) and it will check if the "status" in the JSON response is equal to "Success".
climate:
  - platform: ecodevices_rt2
    host: "192.168.0.20"
    port: 80
    api_key: "XxLzMY69z"
    scan_interval: 5
    friendly_name: Bedroom Heater
    rt2_fp_ext: "1"
    rt2_fp_zone: "1"
```

### Full Example

```yaml
# Example configuration.yaml entry
sensor:
  # Get Elec Index HC
  - <<: &ecodevices_rt2
      platform: ecodevices_rt2
      host: "192.168.0.20"
      port: 80
      api_key: "XxLzMY69z"
      scan_interval: 5
    friendly_name: Elec Index HC
    rt2_command: "Index"
    rt2_command_value: "All"
    rt2_command_entry: "Index_TI1"
    unit_of_measurement: "kWh"
    device_class: "energy"
  # Get Elec Index HP
  - <<: *ecodevices_rt2
    friendly_name: Elec Index HP
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
  - <<: *ecodevices_rt2
    friendly_name: Elec HP/HC
    rt2_command: "Get"
    rt2_command_value: "TI"
    rt2_command_entry: "PTEC"
    unit_of_measurement: ""
    device_class: "None"
  # Get Elec Puissance Appelée
  - <<: *ecodevices_rt2
    friendly_name: Elec Puissance Appelée
    rt2_command: "Get"
    rt2_command_value: "P"
    rt2_command_entry: "INSTANT_POSTE1"
    unit_of_measurement: "kW"
    device_class: "power"

switch:
  - <<: *ecodevices_rt2
    # Get value and change the first EnOcean Switch
    friendly_name: First EnOcean Switch
    rt2_command: "Get"
    rt2_command_value: "XENO"
    rt2_command_entry: "ENO ACTIONNEUR1"
    rt2_on_command: "SetEnoPC"
    rt2_on_command_value: "1"
    rt2_off_command: "ClearEnoPC"
    rt2_off_command_value: "1"
    device_class: "switch"
    icon: "mdi:toggle-switch"

climate:
  - <<: *ecodevices_rt2
    friendly_name: Bedroom Heater
    rt2_fp_ext: "1"
    rt2_fp_zone: "1"
```

[license-shield]: https://img.shields.io/github/license/pcourbin/ecodevices_rt2.svg?style=for-the-badge
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[pre-commit]: https://github.com/pre-commit/pre-commit
[pre-commit-shield]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=for-the-badge
[black]: https://github.com/psf/black
[black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40pcourbin-blue.svg?style=for-the-badge
[buymecoffee]: https://www.buymeacoffee.com/pcourbin
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[user_profile]: https://github.com/pcourbin
