=====
Usage
=====

Generic config
--------------
Default definition of platform in your configuration file:

.. code-block:: yaml

    ecodevices_rt2:
      - name: NameOfYourEcoRT2
        host: "_ADDRESS_IP_"
        port: _PORT_                 # Optional, default: 80
        api_key: "_API_KEY_"
        scan_interval: 5             # Optional, default: 5 (seconds)
        devices:
          - name: Friendly Name Of Entity
            type: "_TYPE_"
            component: "_COMPONENT_"  # Optional
            icon: mdi:water-boiler    # Optional
            device_class: "power"     # Optional
            unit_of_measurement: "W"  # Optional

.. list-table:: Parameter for a the integration `ecodevices_rt2`
   :widths: 20 40 40
   :header-rows: 1

   * - Parameter
     - Description
     - Possible values
   * - `name` (**REQUIRED**)
     - Friendly name of your integration.
     - Any text value
   * - `host` (**REQUIRED**)
     - IP address or hostname where your `GCE Ecodevices RT2`_ is reacheable
     - Any address / hostname
   * - `port`
     - *OPTIONAL* Port associated with the `host`
     - Default: `80`
   * - `api_key` (**REQUIRED**)
     - _API_KEY_ defined on your `GCE Ecodevices RT2`_
     - Any text value
   * - `scan_interval`
     - *OPTIONAL* Time to wait between two updates
     - Any value in second.

       **ATTENTION**, if the value is too low, you may have trouble with the API.
   * - `devices` (**REQUIRED**)
     - List of device definition
     - See next table

.. list-table:: Parameter for a device configuration
   :widths: 20 40 40
   :header-rows: 1

   * - Parameter
     - Description
     - Possible values
   * - `name` (**REQUIRED**)
     - Friendly name of your entity
     - Any text value
   * - `type` (**REQUIRED**)
     - Type of device connected to your Ecodevice RT2
     - `api`, `counter`, `digitalinput`, `enocean`, `post`, `relay`, `supplierindex`, `toroid`, `virtualoutput`, `x4fp`, `xthl`
   * - `component`
     - Type of some default Home Assistant integration
     - `switch`_, `sensor`_, `climate`_, `binary_sensor`_, `light`_
   * - `icon`
     - Icons used by `Home Assistant icons`_
     - Any, some example: `mdi:home`, `mdi:lightbulb`, `mdi:toggle-switch`, etc.
   * - `device_class`
     - Type of `Home Assistant device_class`_
     - Any, some example: `none`, `energy`, `humidity`, `illuminance`, etc.
   * - `unit_of_measurement`
     - Unit of mesurement (`Home Assistant unit_of_measurement`_)
     - Any text value, some example: `W`, `°C`, `kWh`, `lx`, etc.

.. list-table:: Possibles values for device configuration
   :widths: auto
   :header-rows: 1

   * - `type`
     - Default `component`
     - Possible `component`
   * - `api`
     - `sensor`
     - `sensor`, `switch`, `light`
   * - `counter`
     - `sensor`
     - `sensor`
   * - `digitalinput`
     - `binary_sensor`
     - `binary_sensor`
   * - `enocean`
     - `sensor`
     - `sensor`, `switch`, `light`
   * - `post`
     - `sensor`
     - `sensor`
   * - `relay`
     - `switch`
     - `switch`, `light`
   * - `supplierindex`
     - `sensor`
     - `sensor`
   * - `toroid`
     - `sensor`
     - `sensor`
   * - `virtualoutput`
     - `switch`
     - `switch`, `light`
   * - `x4fp`
     - `climate`
     - `climate`, `switch`
   * - `xthl`
     - `sensor`
     - `sensor`

.. _`Home Assistant device_class`: https://www.home-assistant.io/integrations/sensor/#device-class
.. _`Home Assistant icons`: https://www.home-assistant.io/docs/configuration/customizing-devices/#icon
.. _`Home Assistant unit_of_measurement`: https://www.home-assistant.io/docs/configuration/customizing-devices/#unit_of_measurement

.. _`GCE Ecodevices RT2`: http://gce-electronics.com/fr/home/1345-suivi-consommation-ecodevices-rt2-3760309690049.html

.. _`switch`: https://www.home-assistant.io/integrations/switch
.. _`sensor`: https://www.home-assistant.io/integrations/sensor
.. _`climate`: https://www.home-assistant.io/integrations/climate
.. _`climate`: https://www.home-assistant.io/integrations/climate
.. _`binary_sensor`: https://www.home-assistant.io/integrations/binary_sensor
.. _`light`: https://www.home-assistant.io/integrations/light

Advanced/API usage
------------------
To use ecodevices_rt2, you can directly use parameters from the `GCE Ecodevices RT2 API`_ (or `PDF`_).

.. list-table:: Parameters
   :widths: 20 40 40
   :header-rows: 1

   * - `component`
     - Description
     - Parameters
   * - `sensor` (**DEFAULT**)
     - Create a `sensor` which will call `http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&api_get=api_get_value` and get `api_get_entry` in the JSON response.
     - `api_get`: **REQUIRED**.

       `api_get_value`: **REQUIRED**

       `api_get_entry`: **REQUIRED**
   * - `switch` (or `light`)
     - Create a `switch` (or `light`) which will:


       **VALUE** -- To check the current value of the switch, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&api_get=api_get_value and get api_get_entry in the JSON response.


       **ON** -- To change the current value of the switch to ON, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&api_on_get=api_on_get_value and it will check if the "status" in the JSON response is equal to "Success".


       **OFF** -- To change the current value of the switch to OFF, it will call http://_ADDRESS_IP_:_PORT_/api/xdevices.json?key=_API_KEY_&api_off_get=api_off_get_value and it will check if the "status" in the JSON response is equal to "Success".
     - `api_get`: **REQUIRED**

       `api_get_value`: **REQUIRED**

       `api_get_entry`: **REQUIRED**

       `api_on_get`: **REQUIRED**

       `api_on_get_value`: **REQUIRED**

       `api_off_get`: **REQUIRED**

       `api_off_get_value`: **REQUIRED**


----------
Example
----------
.. code-block:: yaml

    ecodevices_rt2:
      - name: NameOfYourEcoRT2
        host: "IP_RT2"
        api_key: "API_KEY_RT2"
        devices:
          - name: Elec Index HC
            type: "api"
            component: "sensor"
            api_get: "Index"
            api_get_value: "All"
            api_get_entry: "Index_TI1"
            device_class: "power"
            unit_of_measurement: "kWh"
            icon: "mdi:flash"

          - name: EnOcean Switch 1
            type: "api"
            component: "switch"
            api_get: "Get"
            api_get_value: "XENO"
            api_get_entry: "ENO ACTIONNEUR1"
            api_on_get: "SetEnoPC"
            api_on_get_value: "1"
            api_off_get: "ClearEnoPC"
            api_off_get_value: "1"

Counter
-------
You can define a Counter (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_)).

.. list-table:: Parameters
   :widths: 20 40 40
   :header-rows: 1

   * - `component`
     - Description
     - Parameters
   * - `sensor` (**DEFAULT**)
     - Create 2 `sensor` which represent a `counter` connected to the `GCE Ecodevices RT2`_:

       `Index` of the counter

       `Price` of the counter
     - `id`: **REQUIRED** Number of the counter (between 1 and 12)


----------
Example
----------
.. code-block:: yaml

    ecodevices_rt2:
      - name: NameOfYourEcoRT2
        host: "IP_RT2"
        api_key: "API_KEY_RT2"
        devices:
          - name: Counter 1
            type: "counter"
            id: 1

DigitalInput
------------
You can define a DigitalInput (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_)).

.. list-table:: Parameters
   :widths: 20 40 40
   :header-rows: 1

   * - `component`
     - Description
     - Parameters
   * - `binary_sensor` (**DEFAULT**)
     - Create a `binary_sensor` which represent a `digitalinput` connected to the `GCE Ecodevices RT2`_
     - `id`: **REQUIRED** Number of the digitalinput (between 1 and 12)


----------
Example
----------
.. code-block:: yaml

    ecodevices_rt2:
      - name: NameOfYourEcoRT2
        host: "IP_RT2"
        api_key: "API_KEY_RT2"
        devices:
          - name: DigitalInput 1
            type: "digitalinput"
            id: 1

EnOcean Switch or Sensor
------------------------
You can define a EnOcean Switch or Sensor (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_)).

.. list-table:: Parameters
   :widths: 20 40 40
   :header-rows: 1

   * - `component`
     - Description
     - Parameters
   * - `sensor` (**DEFAULT**)
     - Create a `sensor` which represent a `enocean` analog sensor connected to the `GCE Ecodevices RT2`_
     - `id`: **REQUIRED** Number of the enocean sensor (between 1 and 24)
   * - `switch`
     - Create a `switch` which represent a `enocean` actuator sensor connected to the `GCE Ecodevices RT2`_
     - `id`: **REQUIRED** Number of the enocean actuator (between 1 and 24)
   * - `light`
     - Create a `light` which represent a `enocean` actuator sensor connected to the `GCE Ecodevices RT2`_
     - `id`: **REQUIRED** Number of the enocean actuator (between 1 and 24)


----------
Example
----------
.. code-block:: yaml

    ecodevices_rt2:
      - name: NameOfYourEcoRT2
        host: "IP_RT2"
        api_key: "API_KEY_RT2"
        devices:
          - name: Bedroom temperature
            type: "enocean"           # Using default component `sensor`
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

Post and Sub-Post
-----------------
You can define a Post and Sub-post (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_)).

.. list-table:: Parameters
   :widths: 20 40 40
   :header-rows: 1

   * - `component`
     - Description
     - Parameters
   * - `sensor` (**DEFAULT**)
     - Create 5 `sensor` which represent a `post` defined on the `GCE Ecodevices RT2`_

       `Index` of the Post/Subpost

       `IndexDay` of the Post/Subpost

       `Price` of the Post/Subpost

       `PriceDay` of the Post/Subpost

       `Instant` power of the Post/Subpost

     - `id`: **REQUIRED** Number of the post (between 1 and 8)

       `subpost`: *OPTIONAL* Number of the subpost of the post (between 1 and 8)


----------
Example
----------
.. code-block:: yaml

    ecodevices_rt2:
      - name: NameOfYourEcoRT2
        host: "IP_RT2"
        api_key: "API_KEY_RT2"
        devices:
          - name: Post 1
            type: "post"
            id: 1
          - name: Subpost 2 of Post 1
            type: "post"
            id: 1
            subpost: 2


Relay
-----
You can define a Relay (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_)).

.. list-table:: Parameters
   :widths: 20 40 40
   :header-rows: 1

   * - `component`
     - Description
     - Parameters
   * - `switch` (**DEFAULT**)
     - Create a `switch` which represent a `relay` connected on the `GCE Ecodevices RT2`_
     - `id`: **REQUIRED** Number of the post (between 1 and 8)
   * - `light`
     - Create a `light` which represent a `relay` connected on the `GCE Ecodevices RT2`_
     - `id`: **REQUIRED** Number of the post (between 1 and 8)


----------
Example
----------
.. code-block:: yaml

    ecodevices_rt2:
      - name: NameOfYourEcoRT2
        host: "IP_RT2"
        api_key: "API_KEY_RT2"
        devices:
          - name: Relay 1
            type: "relay"        # Using default component `sensor`
            id: 1
          - name: Relay 2 as Light
            type: "relay"
            component: "light"
            id: 2

SupplierIndex
-------------
You can define a SupplierIndex (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, SupplierIndex

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # SupplierIndex number 1
    test = SupplierIndex(ecodevices, 1)
    print("Index: %f" % test.value)
    print("Price: %f" % test.price)


Toroid
------
You can define a Toroid (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, Toroid

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # Toroid number 1
    test = Toroid(ecodevices, 1)
    print("Value: %f" % test.value)
    print("Price: %f" % test.price)

    # Only for toroid 1 to 4:
    print("Consumption: %f" % test.consumption)
    print("Consumption Price: %f" % test.consumption_price)
    print("Production: %f" % test.production)
    print("Production Price: %f" % test.production_price)


VirtualOutput
-------------
You can define a VirtualOutput (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, VirtualOutput

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # VirtualOutput number 1
    test = VirtualOutput(ecodevices, 1)
    print("Current status: %r" % test.status)


X4FP (Heaters)
--------------
You can define a X4FP (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, X4FP

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # X4FP of Module 1, Zone 2
    test = X4FP(ecodevices, 1, 2)
    print("Current mode: %d" % test.mode)
    test.mode = 1 # Change mode to `Eco`

.. list-table:: List of Heater/X4FP mode values
   :widths: auto
   :header-rows: 1

   * - Mode
     - State (EN)
     - Etat (FR)
   * - `-1`
     - `UNKNOWN` (or module not present)
     - `UNKNOWN` (ou module non présent)
   * - `0`
     - `Confort`
     - `Confort`
   * - `1`
     - `Eco`
     - `Eco`
   * - `2`
     - `Frost free`
     - `Hors Gel`
   * - `3`
     - `Stop`
     - `Arret`
   * - `4`
     - `Confort -1`
     - `Confort -1`
   * - `5`
     - `Confort -2`
     - `Confort -2`

XTHL
----
You can define a XTHL (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, XTHL

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # XTHL number 1
    test = XTHL(ecodevices, 1)
    print("Temperature: %f" % test.temperature)
    print("Humidity: %f" % test.humidity)
    print("Luminosity: %f" % test.luminosity)

.. _`GCE Ecodevices RT2 API`: https://gce.ovh/wiki/index.php?title=API_EDRT
.. _`PDF`: https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf
