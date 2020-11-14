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

### Simple Example
See [Eco-Devices RT2 API](https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf) for details of `_COMMAND_`, `_PARAMETER_` parameter, and test the resquest in your web browser for `_NAME_`.
```yaml
# Example configuration.yaml entry, which will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&_COMMAND_=_PARAMETER_ and get _NAME_ in the JSON response. 
sensor:
  - platform: ecodevices
    host: "_ADDRESS_IP_"
    port: _PORT_   
    api_key: "_API_KEY_"
    scan_interval: 5
    name: _SENSOR_NAME_IN_HA_
    rt2_in: "_COMMAND_"
    rt2_in_detail: "_PARAMETER_"
    rt2_name: "_NAME_"
    unit_of_measurement: "kW"
    device_class: "power"
```

For example, to get "Index_TI1" which is the first "Télé-Information", the "HC Index".
```yaml
# Example configuration.yaml entry, which will call http://192.168.0.20:80/api/xdevices.json?key=Xx@LzMY69z&Index=All and get "Index_TI1" in the JSON response.
sensor:
sensor:
  - platform: ecodevices
    host: "192.168.0.20"
    port: 80    
    api_key: "XxLzMY69z"
    scan_interval: 5
    name: Elec Index HC
    rt2_in: "Index"
    rt2_in_detail: "All"
    rt2_name: "Index_TI1"
    unit_of_measurement: "kWh" # default=W
    device_class: "power" # default=power
    icon: "mdi:flash" # default=mdi:flash

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
    rt2_in: "Index"
    rt2_in_detail: "All"
    rt2_name: "Index_TI1"
    unit_of_measurement: "kWh"
    device_class: "power"
  # Get Elec Index HP
  - <<: *ecodevices
    name: Elec Index HP
    rt2_in: "Index"
    rt2_in_detail: "All"
    rt2_name: "Index_TI2"
    unit_of_measurement: "kWh"
    device_class: "power"
  # Compute Elec Index, sum of (Elec Index HP) and (Elec Index HC)
  - platform: template
    sensors:
      elec_index:
        friendly_name: "Elec Index"
        unit_of_measurement: "kWh"
        icon_template: "mdi:flash"
        device_class: "power"
        value_template: "{{ states('sensor.elec_index_hp') | float + states('sensor.elec_index_hc') | float }}"
  # Get Elec HP/HC (If your are currently in HP or HC hours, according to your electrical counter)
  - <<: *ecodevices
    name: Elec HP/HC
    rt2_in: "Get"
    rt2_in_detail: "TI"
    rt2_name: "PTEC"
    unit_of_measurement: ""
    device_class: "None"
  # Get Elec Puissance Appelée
  - <<: *ecodevices
    name: Elec Puissance Appelée
    rt2_in: "Get"
    rt2_in_detail: "P"
    rt2_name: "INSTANT_POSTE1"
    unit_of_measurement: "kW"
    device_class: "power"
```
