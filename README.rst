=====================================================
`GCE Ecodevices RT2`_ component for `Home Assistant`_
=====================================================


.. image:: https://img.shields.io/github/license/pcourbin/ecodevices_rt2.svg
        :target: (LICENSE)
        :alt: License

.. image:: https://img.shields.io/badge/HACS-Default-orange.svg
        :target: `hacs`_
        :alt: HACS

.. image:: https://img.shields.io/badge/community-forum-brightgreen.svg
        :target: `forum`_
        :alt: Community Forum

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen
        :target: `pre-commit`_
        :alt: pre-commit

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: `black`_
        :alt: Black

.. image:: https://img.shields.io/badge/maintainer-%40pcourbin-blue.svg
        :target: `user_profile`_
        :alt: Project Maintenance

.. image:: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg
        :target: `buymecoffee`_
        :alt: BuyMeCoffee


This is a *custom component* for `Home Assistant`_ for `GCE Ecodevices RT2`_. This work is based on the work of `Aohzan ipx800`_.
It uses python package `pyecodevices_rt2`_ to call the `GCE Ecodevices RT2 API`_.


- `GCE Ecodevices RT2`_, this repository is for you.
- `GCE Ecodevices`_, see the great work of `Aohzan ecodevices`_.
- `GCE EcodeviceIPX800 V4`_, see the great work of `Aohzan ipx800`_.


`Documentation`_
----------------
See https://pcourbin.github.io/ecodevices_rt2

Full Example
------------

.. code-block:: yaml

 ecodevices_rt2:
  - name: EcoRT2
    host: "192.168.0.20"
    port: 80 # Optional, default: 80
    api_key: #!secret rt2_api_key
    cached_interval_ms: 1000 # Optional, default: 1000ms
    update_after_switch: 1   # Optional, default: 0 (seconds)
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
        type: "enocean"           # Using default component `sensor`
        id: 1
        unit_of_measurement: "°C"
        icon: mdi:thermometer
      - name: EnOcean Switch 1
        type: "enocean"
        component: "switch"
        id: 1
        update_after_switch: 1 # Optional, to define a value for this switch
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
        type: "relay"             # Using default component `sensor`
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
      - name: Toroid 1  # 4 sensors: 2 Consumption + 2 Production
        type: "toroid"
        id: 1
      - name: Toroid 5  # 2 sensors
        type: "toroid"
        id: 5

      #### VirtualOutput Example
      - name: Virtual Output 1
        type: "virtualoutput"      # Using default component `sensor`
        id: 1
      - name: Virtual Output 2 as Light
        type: "virtualoutput"
        component: "light"
        id: 2

      #### X4FP (Heaters) Example
      - name: Heater Module 1 Zone 1
        type: "x4fp"
        component: "climate"       # Can be omitted since default value
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

Credits
-------

| This work is inspired by the work of `Aohzan ipx800`_.
| This repo structure was inspired by `oncleben31/cookiecutter-homeassistant-custom-component`_ project template created with Cookiecutter_.

.. _`GCE Ecodevices RT2`: http://gce-electronics.com/fr/home/1345-suivi-consommation-ecodevices-rt2-3760309690049.html
.. _`GCE Ecodevices RT2 API`: https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf
.. _`GCE Ecodevices`: http://gce-electronics.com/fr/carte-relais-ethernet-module-rail-din/409-teleinformation-ethernet-ecodevices.html
.. _`GCE EcodeviceIPX800 V4`: https://www.gce-electronics.com/fr/carte-relais-ethernet-module-rail-din/1483-domotique-ethernet-webserver-ipx800-v4-3760309690001.html
.. _`Home Assistant`: https://www.home-assistant.io/
.. _`pyecodevices_rt2`: https://github.com/pcourbin/pyecodevices_rt2
.. _`Aohzan ecodevices`: https://github.com/Aohzan/ecodevices
.. _`Aohzan ipx800`: https://github.com/Aohzan/ipx800

.. _`Documentation`: https://pcourbin.github.io/ecodevices_rt2

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`oncleben31/cookiecutter-homeassistant-custom-component`: https://github.com/oncleben31/cookiecutter-homeassistant-custom-component

.. _`hacs`: https://hacs.xyz
.. _`forum`: https://community.home-assistant.io/
.. _`pre-commit`: https://github.com/pre-commit/pre-commit
.. _`black`: https://github.com/psf/black
.. _`user_profile`: https://github.com/pcourbin
.. _`buymecoffee`: https://www.buymeacoffee.com/pcourbin
