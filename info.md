# [GCE Ecodevices RT2](http://gce-electronics.com/fr/home/1345-suivi-consommation-ecodevices-rt2-3760309690049.html) component for [Home Assistant](https://www.home-assistant.io/)

This is a _custom component_ for [Home Assistant](https://www.home-assistant.io/) for [GCE Ecodevices RT2](http://gce-electronics.com/fr/home/1345-suivi-consommation-ecodevices-rt2-3760309690049.html).

If you have:

- [GCE Ecodevices RT2](http://gce-electronics.com/fr/home/1345-suivi-consommation-ecodevices-rt2-3760309690049.html), this package is for you.
- [GCE Ecodevices](http://gce-electronics.com/fr/carte-relais-ethernet-module-rail-din/409-teleinformation-ethernet-ecodevices.html), see the great work of [Aohzan](https://github.com/Aohzan/ecodevices)
- [GCE IPX800 V4](https://www.gce-electronics.com/fr/carte-relais-ethernet-module-rail-din/1483-domotique-ethernet-webserver-ipx800-v4-3760309690001.html), see the great work of [Aohzan](https://github.com/Aohzan/ipx800)

### [Docs (installation, config, and issues)](https://pcourbin.github.io/ecodevices_rt2)

### Features

- Add Counter as sensor (Index and Price)
- Add Digital Input as sensor
- Add EnOcean device as sensor, switch or light
- Add Post/SubPost ad sensor (Index, IndexDay, Price, PriceDay and InstantPower)
- Add Relay as switch or light
- Add SupplierIndex as sensor (Index and Price)
- Add Toroid as sensor (Consumption/Production Index and Price)
- Add Virtual Output as switch or light
- Add X4FP (Heater) as climate or switch
- Add XTHL as sensor (Temperature, Humidity and Luminance)
- Add any sensor/actuator from your EcoRT2 from [Ecodevices RT2 API](https://gce.ovh/wiki/index.php?title=API_EDRT) (or [PDF](https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf))

```yaml
ecodevices_rt2:
  - name: EcoRT2
    host: "192.168.0.20"
    port: 80 # Optional
    api_key: !secret rt2_api_key
    scan_interval: 15
    devices:
      #### API Example
      - name: Elec Index HC (from API)
        type: "api"
        component: "sensor"
        api_get: "Index"
        api_get_value: "All"
        api_get_entry: "Index_TI1"
        device_class: "power"
        unit_of_measurement: "kWh"
        icon: "mdi:flash"
      - name: EnOcean Switch 1 (from API)
        type: "api"
        component: "switch"
        api_get: "Get"
        api_get_value: "XENO"
        api_get_entry: "ENO ACTIONNEUR1"
        api_on_get: "SetEnoPC"
        api_on_get_value: "1"
        api_off_get: "ClearEnoPC"
        api_off_get_value: "1"

      #### Counter Example
      - name: Counter 1
        type: "counter"
        id: 1

      #### DigitalInput Example
      - name: DigitalInput 1
        type: "digitalinput"
        id: 1

      #### EnOcean Switch or Sensor Example
      - name: Bedroom temperature
        type: "enocean" # Using default component `sensor`
        id: 1
        unit_of_measurement: "°C"
        icon: mdi:thermometer
      - name: EnOcean Switch 1
        type: "enocean"
        component: "switch"
        id: 1
      - name: EnOcean Switch 2 as Light
        type: "enocean"
        component: "light"
        id: 2

      #### Post and Sub-Post Example
      - name: Post 1
        type: "post"
        id: 1
      - name: Subpost 2 of Post 1
        type: "post"
        id: 1
        subpost: 2

      #### Relay Example
      - name: Relay 1
        type: "relay" # Using default component `sensor`
        id: 1
      - name: Relay 2 as Light
        type: "relay"
        component: "light"
        id: 2

      #### SupplierIndex Example
      - name: Supplier Index 1 (EDF Info)
        type: "supplierindex"
        id: 1

      #### Toroid Example
      - name: Toroid 1 # 4 sensors: 2 Consumption + 2 Production
        type: "toroid"
        id: 1
      - name: Toroid 5 # 2 sensors
        type: "toroid"
        id: 5

      #### VirtualOutput Example
      - name: Virtual Output 1
        type: "virtualoutput" # Using default component `sensor`
        id: 1
      - name: Virtual Output 2 as Light
        type: "virtualoutput"
        component: "light"
        id: 2

      #### X4FP (Heaters) Example
      - name: Heater Module 1 Zone 1
        type: "x4fp"
        component: "climate" # Can be omitted since default value
        module: 1
        zone: 1
      - name: Heater Module 1 Zone 2 as Switch
        type: "x4fp"
        component: "switch"
        module: 1
        zone: 2

      #### XTHL Example
      - name: XHTL 1
        type: "xthl"
        id: 1
```
