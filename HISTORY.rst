=======
History
=======

2.2.7 (2022-10-10)
-------------------------

* Update version of pyecodevices_rt2, correct X4FP to act like a switch

2.2.6 (2022-08-08)
-------------------------

* Add 'allow_zero' parameters for sensors. Default is True.

2.2.5 (2022-08-08)
-------------------------

* Update version of pyecodevices_rt2, force not to use cache when changing a switch value
* :warning: Toroids are all the same in the new version of the EcoRT2 API: no more "consumption/production" for toroids 1-4.

2.2.4 (2022-08-07)
-------------------------

* Update API using new version EcoRT2 3.00.02
* Reduce errors at startup, wait DataUpdateCoordinator

2.2.2 (beta) (2021-09-18)
-------------------------

* Do not consider `0` for index and price sensors
* Add state classes for energy sensors to be able to use sensors in Energy Management in Home Assistant

2.2.0 (beta) (2021-05-16)
-------------------------

* Test using DataCoordinator

2.1.2 (2021-05-15)
------------------

* Remove scan_interval, not working.
* Add update_after_switch to configure the time to wait before update a switch/light/climate just after a change. Default is 0s.

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
