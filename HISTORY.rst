=======
History
=======

2.1.1 (2021-05-15)
------------------

* Add asyncio.sleep(1) after each switch/light command then force update the current value

2.1.0 (2021-05-15)
------------------

* Update pyecodevices_rt2 to 1.2.0, allow using cached values of the API.
* Add `cached_interval_ms` parameter to define a maximum value (in milliseconds) during which you consider an API value do not need to be updated
* Improve the time between switch/light action and value update

2.0.0 (2021-05-06)
------------------

* Full rewrite using platform/devices
* Allow adding devices/entities without knowing the API: counter, digitalinput, enocean, post, relay, supplierindex, toroid, virtualoutput, x4fp, xthl
* Allow selecting different components (e.g. for `enocean`, you can select `sensor`, `switch` or `light`)

1.0.1 (2021-05-01)
------------------

* First stable version with updated version and pyecodevices-rt2 package

0.1.0 (2021-04-08)
------------------

* First version
