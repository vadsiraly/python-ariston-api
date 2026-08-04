"""Evo device class for Ariston module."""

from __future__ import annotations

import logging

from .const import (
    EvoDeviceProperties,
    LuxPlantMode,
    PlantData,
    WaterHeaterMode,
)
from .evo_device import AristonEvoDevice

_LOGGER = logging.getLogger(__name__)


class AristonLydosDevice(AristonEvoDevice):
    """Class representing a physical Lydos Wi-Fi device, it's state and properties."""

    @property
    def water_heater_mode(self) -> type[WaterHeaterMode]:
        """Return the water heater mode class"""
        return LuxPlantMode

    @property
    def plant_data(self) -> PlantData:
        """Final string to get plant data"""
        return PlantData.Se

    def set_water_heater_operation_mode(self, operation_mode: str):
        """Set water heater operation mode"""
        self.api.set_evo_mode(self.gw, self.water_heater_mode[operation_mode])
        self.data[EvoDeviceProperties.MODE] = self.water_heater_mode[
            operation_mode
        ].value

    async def async_set_water_heater_operation_mode(self, operation_mode: str):
        """Async set water heater operation mode"""
        await self.api.async_set_evo_mode(
            self.gw, self.water_heater_mode[operation_mode]
        )
        self.data[EvoDeviceProperties.MODE] = self.water_heater_mode[
            operation_mode
        ].value

    @property
    def boost_req_temp_value(self) -> float | None:
        """Get water heater boost requested temperature"""
        from .const import LydosDeviceProperties
        return self.data.get(LydosDeviceProperties.BOOST_REQ_TEMP, None)

    async def async_set_water_heater_boost_req_temp(self, temperature: float):
        """Async set water heater boost requested temperature"""
        from .const import LydosDeviceProperties
        await self.api.async_set_lydos_boost_temperature(self.gw, temperature)
        self.data[LydosDeviceProperties.BOOST_REQ_TEMP] = temperature
