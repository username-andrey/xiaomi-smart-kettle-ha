from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .entity import KettleEntity

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    async_add_entities([KettleStopButton(entry.runtime_data)])

class KettleStopButton(KettleEntity, ButtonEntity):
    _attr_translation_key = "stop"
    def __init__(self, coordinator):
        super().__init__(coordinator, "stop")
    async def async_press(self) -> None:
        await self.coordinator.async_action(3, 1)
