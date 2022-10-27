import asyncio
from winrt.windows.devices import radios

async def BluetoothOn(turn_on):
    all_radios = await radios.Radio.get_radios_async()
    for this_radio in all_radios:
        if this_radio.kind == radios.RadioKind.BLUETOOTH:
            if "on" in turn_on:
                await this_radio.set_state_async(radios.RadioState.ON)
            else:
                await this_radio.set_state_async(radios.RadioState.OFF)

def onoff(ans):
    if "on" in ans:
        if __name__ == "__main__":
            asyncio.run(BluetoothOn("on"))

    else:
        if __name__ == "__main__":
            asyncio.run(BluetoothOn("off"))

